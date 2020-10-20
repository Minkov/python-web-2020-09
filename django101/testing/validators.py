from django.core.exceptions import ValidationError


def contains_only_digits_validator(value):
    result = all(x.isdigit() for x in value)
    if not result:
        raise ValidationError('EGN should contain only digits')
