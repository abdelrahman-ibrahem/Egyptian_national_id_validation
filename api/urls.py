from django.urls import path
from . import views

urlpatterns = [
    path('validate/', views.ValidateIDView.as_view(), name='validate-id'),
    path('logs/', views.ListLogs.as_view(), name='api-request-logs'),
]