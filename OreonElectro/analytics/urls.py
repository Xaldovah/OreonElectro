from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
        path('activities', views.UserActivityListView.as_view(), name='activity_list'),
        path('log-activity/', views.LogUserActivityView.as_view(), name='log_activity'),
        path('sales-overview/', views.SalesOverviewView.as_view(), name='sales_overview'),
        path('customer-behavior/', views.CustomerBehaviorView.as_view(), name='customer_behavior'),
        path('general-metrics/', views.GeneralMetricsView.as_view(), name='general_metrics'),
]
