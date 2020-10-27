from django.core.exceptions import ValidationError


def validate_does_contain_spaces(value):
    result = any(' ' in x for x in value)
    if result:
        raise ValidationError('Cannot contain spaces')
