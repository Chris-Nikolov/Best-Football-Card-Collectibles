from django.core.exceptions import ValidationError


def name_validator(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Your name must contain only letters.")
