from django import template

register = template.Library()

@register.filter
def specifyLangEn(value):
    return value.replace('{lang}', 'en')