import misaka
from misaka import html, HTML_HARD_WRAP, HTML_TOC, EXT_AUTOLINK, EXT_TABLES
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def markdown(text):
    return mark_safe(html(
        text,
        extensions=EXT_AUTOLINK | EXT_TABLES,
        render_flags=HTML_HARD_WRAP | HTML_TOC
        ))
