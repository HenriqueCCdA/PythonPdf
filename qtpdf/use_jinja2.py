import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./template")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("laudo.html")

tabela = {
    'Tecido1': {'dose': 3.1, 'mass': 1.8},
    'Tecido2': {'dose': 4.1, 'mass': 1.0}
}

data = {'paciente': 'Nome', 'isotopo': 'I-131', 'tabela': tabela}
outputText = template.render(**data)

print(outputText)