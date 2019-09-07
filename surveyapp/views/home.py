import json
import random

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from surveyapp.models import SurveyModel, ResponsesModel, QuestionsModel


def home(request):
    data = dict()
    data["is_home_page"] = True
    return render(request, 'surveyapp/home.html', data)


def survey_add(request):
    data = dict()

    if "GET" == request.method:
        return render(request, 'surveyapp/survey_add.html', data)

    # else for POST method
    post_data = request.POST

    q_data_str = post_data["data"]

    # list of questions in json object format
    q_dict = json.loads(q_data_str)

    uuid = get_random_string()
    survey_model = SurveyModel()
    survey_model.uuid = uuid
    survey_model.title = post_data["survey_title"]
    survey_model.data = q_data_str
    survey_model.created_at = timezone.now()
    survey_model.save()

    data["is_success"] = True
    data["survey_url"] = request.build_absolute_uri(reverse('surveyapp:survey_fill', args=[uuid, ]))

    return JsonResponse(data)


def survey_fill(request, uuid):
    data = dict()

    survey_instance = SurveyModel.objects.get(uuid=uuid)

    if "GET" == request.method:
        data["survey"] = survey_instance
        data["qdata"] = json.loads(survey_instance.data)
        return render(request, "surveyapp/survey_fill.html", data)

    # else for post data, collect response and save to DB
    post_data = request.POST
    print(post_data)
    for key, value in post_data.lists():
        if key == "csrfmiddlewaretoken":
            continue

        try:
            question_instance = QuestionsModel.objects.get(fid=key)
        except Exception as e:
            pass
        response = ResponsesModel()
        response.survey_id = survey_instance.sys_id
        response.q_id = 11  # question_instance.sys_id
        response.response = value[0] if len(value) == 1 else value
        response.created_by = ""
        response.created_at = timezone.now()
        response.save()

    messages.success(request, "Response submitted successfully")

    return render(request, 'surveyapp/home.html', data)


def survey_response_all(request):
    data = dict()
    surveys = SurveyModel.objects.all()
    data["surveys"] = surveys
    return render(request, 'surveyapp/survey_response_all.html', data)


def survey_response_one(request, uuid):
    data = dict()
    survey_instance = SurveyModel.objects.get(uuid=uuid)
    responses = ResponsesModel.objects.filter(survey_id=survey_instance.sys_id)
    data["responses"] = responses
    data["survey"] = survey_instance

    return render(request, 'surveyapp/survey_response_one.html', data)


def get_random_string(length=6):
    letters = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    return ''.join(random.SystemRandom().choice(letters) for _ in range(length))
