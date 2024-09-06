from django.forms import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')
        
def file_max_size_validator(max_size):
    def validate(value):
        filesize = value.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %MB" % str(megabyte_limit))
    return validate