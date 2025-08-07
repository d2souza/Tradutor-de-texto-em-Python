from deep_translator import GoogleTranslator

class TranslatorService:

    def translate_text(self, text, src, dest):
        try:
            translate_text = GoogleTranslator(source=src, target=dest).translate(text)
            return translate_text
        except Exception as e:
            return f"Erro ao traduzir: {str(e)}"

