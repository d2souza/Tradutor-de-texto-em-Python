import sys
from PyQt5.QtWidgets import QApplication
from ui_main import TranslatorUi
from translator import TranslatorService

class TranslatorApp(TranslatorUi):
    def __init__(self):
        super().__init__()
        self.translator_service = TranslatorService()
        self.translate_button.clicked.connect(self.translate)

    def translate(self):
        text = self.input_text.toPlainText()
        src_lang = self.src_lang.currentData()
        dest_lang = self.dest_lang.currentData()

        translated = self.translator_service.translate_text(text, src_lang, dest_lang)
        self.output_text.setText(translated)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())