

import metadata
import website.templates as templates
import website.html as html

def generate(airium):
    a = airium
    with templates.html(a):
        templates.head(a)
        with a.body():
            templates.topbar(a)
            with html.centered(a, 500, 300):
                with html.centered(a, 100, 'auto'):
                    with a.h3():
                        a(metadata.project_name)
                a(metadata.sales_pitch)
            templates.firebase(a)
            templates.footer(a)
    return str(a)
