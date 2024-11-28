from django.core.exceptions import ValidationError


def name_validator(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Your name must contain only letters.")


def phone_validator(value):
    if not (x.isdigit() for x in value) or len(value) != 10:
        raise ValidationError("Invalid phone number.")


def validate_profile_picture_size(image):
    max_size_kb = 500
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image size must not exceed {max_size_kb} KB.")
