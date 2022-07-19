import sys

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLineEdit,
                             QMessageBox,
                             QLabel)
from PyQt5.QtCore import QSizeF
from jinja2 import FileSystemLoader, Environment


def jinja2_context_processor(template_dir, template_name):
    templateLoader = FileSystemLoader(searchpath="./template")
    templateEnv = Environment(loader=templateLoader)
    return templateEnv.get_template("laudo.html")


class Jinja2ContextProcessor:
    def __init__(self, template_dir, template_name):
        self.searchpath = template_dir
        self.template_name = template_name
        self._setup()

    def _setup(self):
        templateLoader = FileSystemLoader(searchpath=self.searchpath)
        templateEnv = Environment(loader=templateLoader)
        self.template = templateEnv.get_template(self.template_name)

    def render(self, **kargs):
        return self.template.render(kargs)


def print_pdf(pdf_path):

    printer = QPrinter(QPrinter.PrinterResolution)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setPaperSize(QPrinter.A4)
    marginleft = 10
    marginright = 10
    margintop = 10
    marginbottom = 10
    printer.setPageMargins(marginleft, marginright, margintop, marginbottom, QPrinter.Millimeter)

    printer.setOutputFileName(pdf_path)

    doc = QTextDocument()

    tabela = {
        'Tecido1': {'dose':  3.1, 'mass': 1.8},
        'Tecido2': {'dose':  4.1, 'mass': 1.0},
        'Tecido3': {'dose': 10.1, 'mass': 5.0}
    }

    data = {'paciente': 'Paciente nome',
            'isotopo': 'I-131',
            'tabela': tabela,
            'dvh': './data/dvh.png'}
    template = Jinja2ContextProcessor(template_dir='./template', template_name='report.html')
    html = template.render(**data)

    doc.setHtml(html)
    doc.setPageSize(QSizeF(printer.pageRect().size()))
    doc.print(printer)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerar Pdf')
        self.setGeometry(50, 50, 400, 50)
        self.UI()

    def UI(self):

        vbox = QVBoxLayout()
        hbox_top = QHBoxLayout()
        hbox_base = QHBoxLayout()

        vbox.addStretch()
        vbox.addLayout(hbox_top)
        vbox.addLayout(hbox_base)
        vbox.addStretch()

        label = QLabel('nome do arquivo pdf:')
        self.input = QLineEdit()
        hbox_top.addStretch()
        hbox_top.addWidget(label)
        hbox_top.addWidget(self.input)
        hbox_top.addStretch()

        btn = QPushButton('Gerar pdf', self)
        btn.clicked.connect(self.on_btn)

        hbox_base.addStretch()
        hbox_base.addWidget(btn)
        hbox_base.addStretch()

        self.setLayout(vbox)

        self.show()

    def on_btn(self):
        name = self.input.text().strip()
        if name.endswith('.pdf'):
            print_pdf(pdf_path=name)
            QMessageBox.information(self, 'Arquivo gerado', f'Arquivo {name} gerado.')
        elif not name:
            QMessageBox.warning(self, 'Nome invalido', 'Nome do arquivo vazio.')
        else:
            QMessageBox.warning(self, 'Nome invalido', 'O arquivo tem que termina com .pdf.')



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())