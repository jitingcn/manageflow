from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def site_name():
    return settings.SITE_NAME


@register.simple_tag
def site_root():
    return settings.SITE_ROOT


@register.simple_tag
def site_scheme():
    parts = settings.SITE_ROOT.split("://")
    assert parts[0] in ("http", "https")
    return parts[0]


@register.simple_tag
def site_hostname():
    parts = settings.SITE_ROOT.split("://")
    return parts[1]


@register.simple_tag
def site_version():
    return settings.VERSION


@register.simple_tag
def nav_css_class(page_class):
    if not page_class:
        return ""
    else:
        return page_class
