from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import requests
import hashlib
from .models import Diagnosis
from django.views.decorators.csrf import csrf_exempt
from json import loads
import boto3


def index(request: HttpRequest):
    processed_results = Diagnosis.objects.all().values_list('patient_name', 'diagnosis_percentage')
    return render(request, 'index.html', context={'query_results': processed_results})


def get_pasha(request: HttpRequest):
    responce = requests.get('http://storage.yandexcloud.net/bucketyar/022.png')
    return HttpResponse(responce.content, content_type='image/png')


@csrf_exempt
def add_diagnosis(request: HttpRequest):
    data = loads(request.body)
    print(data)
    Diagnosis.objects.create(patient_name=data.get('patient_name'), diagnosis_percentage=data.get('diagnosis_percentage'))
    return HttpResponse('OK')


@csrf_exempt
def add_file(request: HttpRequest):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )

    file_content = request.body
    print(file_content[:20], len(file_content))

    s3.put_object(Bucket='bucketyar', Key=f'{hashlib.md5(file_content).hexdigest()}', Body=file_content, StorageClass='COLD')

    # responce = requests.put(f'http://storage.yandexcloud.net/bucketyar/{hashlib.md5(file_content).hexdigest()}', data=file_content)
    return HttpResponse('OK')
