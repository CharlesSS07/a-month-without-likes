

import metadata
import templates

page_path = 'index.html'

def generate(airium):
    a = airium
    with templates.html(a):
        templates.head(a)
        templates.topbar(a)
        with a.h3(id="id23409231", klass='main_header'):
            a("Hello World.")
        templates.footer(a)
    return str(a)
