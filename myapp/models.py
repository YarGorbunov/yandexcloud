import datetime

from django.db import models
from django.utils import timezone


class Diagnosis(models.Model):
    patient_name = models.CharField(max_length=100, blank=True)
    diagnosis_percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.patient_name
