from django.conf import settings
from django.shortcuts import render
from django.utils import timezone


def about(request):
    data = dict()
    data["this_title"] = "About Us"    
    return render(request, 'surveyapp/others/about.html', data)


def contact(request):
    data = dict()
    data["this_title"] = "Contact Us"
    return render(request, 'surveyapp/others/contact.html', data)


def terms(request):
    data = dict()
    data["this_title"] = "Terms and conditions"
    return render(request, 'surveyapp/others/terms.html', data)


def privacy(request):
    data = dict()
    data["this_title"] = "Privacy Policy"
    return render(request, 'surveyapp/others/privacy.html', data)



