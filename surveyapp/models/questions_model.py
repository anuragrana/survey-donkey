from django.db import models


class SurveyModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    uuid = models.CharField(null=False, blank=False, max_length=6, unique=True)
    title = models.CharField(null=False, blank=False, max_length=100)
    data = models.TextField(null=False, blank=True)
    color_scheme = models.CharField(null=True, blank=True, max_length=10)
    q_per_page = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=True)
    last_accessed_at = models.DateTimeField(null=True, blank=True)
    hit_count = models.BigIntegerField(default=0, null=False, blank=True)

    class Meta:
        app_label = "surveyapp"
        db_table = "survey"

    def __str__(self):
        return self.uuid + " : " + self.title


class QuestionsModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    # frontend id
    fid = models.CharField(null=False, blank=False, max_length=6)
    q_text = models.CharField(null=False, blank=False, max_length=1024)
    q_type = models.CharField(null=False, blank=False, max_length=2)
    survey = models.ForeignKey('SurveyModel', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = "surveyapp"
        db_table = "questions"


# options of radio button or checkbox
class OptionsModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    # frontend id
    fid = models.CharField(null=False, blank=False, max_length=6)
    q_text = models.CharField(null=False, blank=False, max_length=1024)
    question = models.ForeignKey('QuestionsModel', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = "surveyapp"
        db_table = "options"


class ResponsesModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    survey_id = models.IntegerField(null=False, blank=True)
    q_id = models.IntegerField(null=False, blank=True)
    response = models.TextField(null=False, blank=True)
    created_by = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "surveyapp"
        db_table = "responses"
