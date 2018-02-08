import re
from django.forms import ValidationError


def phone_number_validator(value):
    print("This is Validator!!!!!!!!!!!!!!!!!!!!!!!")
    p = re.compile('^01\d{8,9}$')
    if not re.match(value):
        raise ValidationError('{} is not proper phone number'.format(value))
