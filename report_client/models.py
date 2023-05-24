from django.db import models


# Create your models here.
class Report(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    creation_date = models.CharField()
    report_date = models.CharField()
    time_span_minutes = models.IntegerField()
    task_name = models.CharField()
    task_description = models.CharField()
