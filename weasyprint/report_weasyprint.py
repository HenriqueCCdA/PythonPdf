from weasyprint import CSS, HTML
from jinja2 import FileSystemLoader, Environment


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


template = Jinja2ContextProcessor(template_dir='template', template_name='report.html')


tabela = {
    'Whole Body': {'dose':  0.25, 'mass': 18.38},
    'Lungs': {'dose': 0.82, 'mass': 0.55},
    'Liver': {'dose': 1.65, 'mass': 1.42},
    'Bones': {'dose': 1.65, 'mass': 1.42},
    'Liver': {'dose': 0.18, 'mass': 1.23},
    'Air': {'dose': 0.22, 'mass': 0.03},
    'LKidney': {'dose': 3.46, 'mass': 0.18},
    'RKidney': {'dose': 2.90, 'mass': 0.20},
    'Spleen': {'dose': 6.03, 'mass': 0.12},
    'Tumour1': {'dose': 11.82, 'mass': 0.25},
}

data = {'paciente': 'Paciente_clycle',
        'isotopo': 'I-131',
        'clinica': 'PEN0/COPPE/UFRJ',
        'data': '03/04/2021',
        'tabela': tabela,
        'dvh': '../data/dvh.png'}

html = HTML(string=template.render(**data), base_url='template/')

css = CSS(filename='template/css/report.css', base_url='template/')

html.write_pdf('report_teste.pdf', stylesheets=[css])