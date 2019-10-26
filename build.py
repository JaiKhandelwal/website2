from jinja2 import Template
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

objs = { "index.html"}

for obj in objs:
    template = env.get_template(obj)
    with open(obj, "w") as fp:
        fp.write(template.render())
