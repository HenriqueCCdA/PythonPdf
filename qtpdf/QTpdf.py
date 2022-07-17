import sys
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QSizeF



def read_html_template(path='template/laudo.html'):
    with open(path, 'r') as f:
        html_template = f.read()

    return html_template

def read_table_from(path='data/dvh.txt'):
    with open(path, 'r') as f:
        lines = f.readlines()

    tissues = {}
    for l in lines:
        name, v = l.split()
        tissues[name] = v
    return tissues


def print_pdf(pdf_path):
    pdf_path = './teste.pdf'

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

    html = read_html_template()
    tissues = read_table_from()

    print(tissues, html)

    doc.setHtml(html)
    doc.setPageSize(QSizeF(printer.pageRect().size()))  # hide the page number
    doc.print(printer)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gera Pdf')
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):

        btn = QPushButton('Gera pdf', self)

        btn.clicked.connect(self.on_btn)

        self.show()

    def on_btn(self):
        print_pdf(pdf_path='teste.pf')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())