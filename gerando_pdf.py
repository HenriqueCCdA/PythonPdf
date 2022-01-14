from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


nome_pdf = 'teste'

pdf = canvas.Canvas(f'{nome_pdf}.pdf', pagesize=letter)
pdf.setFont("Helvetica", 12)

x_min, x_max = 0, letter[0]
y_min, y_max = 0, letter[1]

pdf.setTitle(nome_pdf)

#
pdf.setFont("Helvetica", 14)
pdf.drawString(x_max/2 - 50, y_max - 145 , 'Laudo de Tomografia')
#

#
pdf.drawString(50, y_max - 185 , 'Nome:')
pdf.drawString(50, y_max - 235 , 'Data do exame:')
pdf.drawString(50, y_max - 285 , 'Empresa:')
#
pdf.drawString(300, y_max - 185 , 'Indicação:')
pdf.drawString(300, y_max - 235 , 'Data de Nascimento:')
pdf.drawString(300, y_max - 285 , 'Sexo:')


pdf.line(x_min + 20, y_min + 20, x_min + 20, y_max - 20)
pdf.line(x_max - 20, y_min + 20, x_max - 20, y_max - 20)
# Topo
pdf.line(x_min + 20, y_max - 20, x_max - 20, y_max - 20)
pdf.line(x_min + 20, y_max - 120, x_max - 20, y_max - 120)

pdf.line(x_min + 200, y_max - 120, x_min + 200, y_max - 20)
pdf.line(x_max - 200, y_max - 120, x_max - 200, y_max - 20)

# Tipo do laudo
heigth = 160
pdf.line(x_min + 20, y_max - 160, x_max - 20, y_max - 160)

# dados
heigth = 300
pdf.line(x_min + 20, y_max - heigth, x_max - 20, y_max - heigth)
# Base
pdf.line(x_min + 20, y_min + 60, x_max - 20, y_min + 60)
pdf.line(x_min + 20, y_min + 20, x_max - 20, y_min + 20)


pdf.save()