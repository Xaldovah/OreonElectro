from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Language, Translation
from .serializers import LanguageSerializer, TranslationSerializer


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
        translations = Translation.objects.all()
        serializer = TranslationSerializer(translations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TranslationDetailView(APIView):
    """
    Translation detail view class
    """
    def get(self, request, text, language_code):
        try:
            language = Language.objects.get(code=language_code)
            translation = Translation.objects.get(text=text, language=language)
            serializer = TranslationSerializer(translation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (Language.DoesNotExist, Translation.DoesNotExist):
            return Response({'error': 'Translation not found.'}, status=status.HTTP_404_NOT_FOUND)
