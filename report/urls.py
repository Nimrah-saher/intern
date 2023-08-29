from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_submission, name='work_submission'),
    # Define other URL patterns for the report app here
]