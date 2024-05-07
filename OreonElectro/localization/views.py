from django.utils import timezone
from django.utils.formats import localize
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Language, Translation
from .serializers import LanguageSerializer, TranslationSerializer
from django.utils.translation import activate, get_language_from_request
import babel.numbers
from babel.dates import format_datetime


class LanguageListView(APIView):
    """
    Language list view class
    """
    def get(self, request):
        languages = Language.objects.filter(is_active=True)
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TranslationListView(APIView):
    """
    Translation list view class
    """
    def get(self, request):
        lang_code = request.query_params.get('lang', get_language_from_request(request))
        activate(lang_code)

        translations = Translation.objects.select_related('language').all()
        serializer = TranslationSerializer(translations, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TranslationDetailView(APIView):
    """
    Translation detail view class
    """
    def get(self, request, text, language_code):
        try:
            language = Language.objects.get(code=language_code)
            activate(language_code)

            translation = Translation.objects.get(text=text, language=language)
            serializer = TranslationSerializer(translation, context={'request': request})

            example_amount = 1234.56
            formatted_amount = babel.numbers.format_currency(example_amount, 'USD', locale=language_code)

            current_time = timezone.now()
            formatted_date = format_datetime(current_time, locale=language_code)

            return Response({
                'translation': serializer.data,
                'formatted_amount': formatted_amount,
                'formatted_date': formatted_date
            }, status=status.HTTP_200_OK)
        except (Language.DoesNotExist, Translation.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
