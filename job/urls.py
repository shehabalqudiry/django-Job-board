from django.urls import path
from . import views, api

app_name = 'job'
urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add',views.add_job, name='add_job'),
    path('<slug:slug>', views.job_detail, name='job_detail'),
    path('api/list', api.joblistapi, name='joblistapi'),
]
