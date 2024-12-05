from django.core.exceptions import ValidationError


def validate_image_size(image):
    if isinstance(image, bool) or not hasattr(image, 'size'):
        return
    max_size_kb = 800
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image size must not exceed {max_size_kb} KB.")
