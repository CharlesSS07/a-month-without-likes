

import metadata
import website.templates as templates
import website.html as html

def generate(airium):
    a = airium
    with templates.html(a):
        
        def head_extension(a):
            a.script(src='https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.js')
            a.link(type="text/css", rel="stylesheet", href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css")
        
        templates.head(a, extension=head_extension)
        
        with a.body():
            templates.topbar(a)
            with html.centered(a, 500, 300):
                with html.centered(a, 100, 'auto'):
                    with a.h3():
                        a(metadata.project_name)
                a('''<div id="firebaseui-auth-container"></div>
<div id="loader">Loading...</div>''')
#            templates.firebase(a)
            a.script(type='module', src='/static/login.js')
            templates.footer(a)
    return str(a)

