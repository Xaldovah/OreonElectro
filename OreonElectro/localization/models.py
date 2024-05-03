from django.db import models


class Language(models.Model):
    """
    Represents a language for localization.

    Attributes:
        name (str): The name of the language.
        code (str): The code for the language (e.g., 'en', 'fr', 'es').
        is_active (bool): Whether the language is active or not.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Translation(models.Model):
    """
    Represents a translation for a specific text.

    Attributes:
        text (str): The original text to be translated.
        language (Language): The language for which the translation is provided.
        translation (str): The translated text.

    """
    text = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='translations')
    translation = models.TextField()

    
    class Meta:
        unique_together = ('text', 'language')

    def __str__(self):
        return f"{self.text} ({self.language.code})"
