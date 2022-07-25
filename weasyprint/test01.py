from weasyprint import CSS, HTML


HTML('http://weasyprint.org/').write_pdf('test01_a.pdf')

HTML('http://weasyprint.org/').write_pdf('test01_b.pdf', stylesheets=[CSS(string='body {font-family: serif !importan')])