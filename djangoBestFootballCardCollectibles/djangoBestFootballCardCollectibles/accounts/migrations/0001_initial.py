# Generated by Django 5.1.3 on 2024-12-01 13:10

import cloudinary.models
import django.core.validators
import django.db.models.deletion
import djangoBestFootballCardCollectibles.accounts.models
import djangoBestFootballCardCollectibles.accounts.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BFCCUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', djangoBestFootballCardCollectibles.accounts.models.BFCCUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, null=True, validators=[djangoBestFootballCardCollectibles.accounts.validators.name_validator, django.core.validators.MaxLengthValidator(25), django.core.validators.MinLengthValidator(2)], verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, null=True, validators=[djangoBestFootballCardCollectibles.accounts.validators.name_validator, django.core.validators.MaxLengthValidator(25), django.core.validators.MinLengthValidator(2)], verbose_name='Last Name')),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[djangoBestFootballCardCollectibles.accounts.validators.validate_profile_picture_size], verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('phone_number', models.CharField(blank=True, null=True, validators=[djangoBestFootballCardCollectibles.accounts.validators.phone_validator], verbose_name='Phone Number')),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(300)], verbose_name='Description')),
            ],
        ),
    ]