from django.conf import settings


# context processor can be used to pass some parameter to all templates from one place
def site(request):
    data = dict()
    data["project_name"] = settings.PROJECT_NAME
    data["project_name_spaces"] = settings.PROJECT_NAME_SPACED
    data["site_url"] = settings.SITE_URL
    data["project_name_short"] = settings.PROJECT_NAME_SHORT
    data["tagline"] = settings.TAGLINE
    data["page_canonical_url"] = request.build_absolute_uri()
    return data
