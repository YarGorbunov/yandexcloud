from django.urls import path

from . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pasha', views.get_pasha, name='get_pasha'),
    path('add-diagnosis', views.add_diagnosis, name='add_diagnosis'),
    path('add-file', views.add_file, name='add_file'),
]
