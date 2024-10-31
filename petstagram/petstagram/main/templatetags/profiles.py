
from django import template

from petstagram.accounts.models import Profile


register = template.Library()

@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0