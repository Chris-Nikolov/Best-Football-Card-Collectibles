from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from djangoBestFootballCardCollectibles.accounts.validators import (name_validator, phone_validator,
                                                                    validate_profile_picture_size, )


class BFCCUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class BFCCUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BFCCUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(BFCCUser, primary_key=True, on_delete=models.CASCADE)

    first_name = models.CharField(validators=[name_validator, MaxLengthValidator(25), MinLengthValidator(2)],
                                  verbose_name="First Name", null=True, blank=True)

    last_name = models.CharField(validators=[name_validator, MaxLengthValidator(25), MinLengthValidator(2)],
                                 verbose_name="Last Name", null=True, blank=True)

    profile_picture = CloudinaryField('image', blank=True, null=True, validators=[validate_profile_picture_size], )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    address = models.TextField(verbose_name="Address", blank=True, null=True)

    phone_number = models.CharField(verbose_name="Phone Number", validators=[phone_validator], blank=True, null=True)

    description = models.TextField(verbose_name="Description", blank=True, null=True,
                                   validators=[MaxLengthValidator(300)])

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return "/static/images/base_profile_picture.png/"
