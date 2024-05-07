from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
        path('', views.NotificationListView.as_view(), name='notification_list'),
        path('mark-as-read/<int:notification_id>/', views.MarkNotificationAsReadView.as_view(), name='mark_as_read'),
        path('create/', views.CreateNotificationView.as_view(), name='create_notification'),
]
