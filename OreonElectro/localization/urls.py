from django.urls import path
from . import views

app_name = 'localization'

urlpatterns = [
        path('languages/', views.LanguageListView.as_view(), name='language_list'),
        path('translations/', views.TranslationDetailView.as_view(), name='translation_detail')
]
