from django.urls import path
from . import views

app_name = 'localization'

urlpatterns = [
        path('languages/', views.LanguageListView.as_view(), name='language_list'),
        path('translations/', views.TranslationListView.as_view(), name='translation_list'),
        path('translation/<str:text>/<str:language_code>/', views.TranslationDetailView.as_view(), name='translation_detail')
]
