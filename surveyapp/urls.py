from django.urls import path

from . import views

app_name = "surveyapp"
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'survey/add/', views.survey_add, name='survey_add'),

    path(r'survey/responses/', views.survey_response_all, name='survey_response_all'),
    path(r'survey/responses/<slug:uuid>/', views.survey_response_one, name='survey_response_one'),
    # this should be last path due to slug
    path(r'survey/<slug:uuid>/', views.survey_fill, name='survey_fill'),
]

urlpatterns += [
    path(r'page/about-us/', views.about, name='about'),
    path(r'page/contact-us/', views.contact, name='contact'),
    path(r'page/terms/', views.terms, name='terms'),
    path(r'page/privacy/', views.privacy, name='privacy'),
]
