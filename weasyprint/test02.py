from weasyprint import CSS, HTML


html = HTML(string='''<h1>The title</h1>
    <p>Content goes here</p>
''')

css = CSS(string='@page {size: A4; margin: 1cm} ')

html.write_pdf('test02.pdf', stylesheets=[css])