from django.conf import settings

def template_vars(request):
    """
    This function passes global variables to all templates
    """
    return dict(
            CAMP_NAME=settings.CAMP_NAME,
            )
