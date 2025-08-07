from PyQt5.QtWidgets import(
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QTextEdit,
    QPushButton,
)

class TranslatorUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tradutor com Python")
        self.setMinimumSize(400,300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        lang_layout = QHBoxLayout()
        self.src_lang = QComboBox()
        self.dest_lang = QComboBox()

        langs = {
            'Português': 'pt',
            'Inglês': 'en',
            'Espanhol': 'es',
            'Francês': 'fr',
            'Alemão': 'de',
            'Italiano': 'it',
        }

        for lang in langs:
            self.src_lang.addItem(lang, langs[lang])
            self.dest_lang.addItem(lang, langs[lang])

        self.src_lang.setCurrentText('Português Brasileiro')
        self.dest_lang.setCurrentText('Inglês')

        lang_layout.addWidget(QLabel("De:"))
        lang_layout.addWidget(self.src_lang)
        lang_layout.addWidget(QLabel("Para:"))
        lang_layout.addWidget(self.dest_lang)
        self.layout.addLayout(lang_layout)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Digite o texto aqui...")
        self.layout.addWidget(self.input_text)

        self.translate_button = QPushButton("Traduzir")
        self.layout.addWidget(self.translate_button)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout.addWidget(self.output_text)