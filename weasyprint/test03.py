from weasyprint import CSS, HTML

import logging
logger = logging.getLogger('weasyprint')
breakpoint()
logger.warning('Print')

html = HTML(string='''<h1>The title</h1>
    <p>Content goes here</p>
''')

css = CSS(string='@page {size: A4; margin: 1cm} ')

html.write_pdf('test03.pdf', stylesheets=[css])