from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
        path('activities/', views.UserActivityListView.as_view(), name='activity_list'),
        path('log-activity/', views.LogUserActivityView.as_view(), name='log_activity'),
]
