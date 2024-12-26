from django.contrib import admin

from .models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'diagnosis_percentage')

admin.site.register(Diagnosis, DiagnosisAdmin)
