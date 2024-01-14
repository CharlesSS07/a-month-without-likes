
import metadata

def html(airium, lang='en')
    a('<!DOCTYPE html>')
    return a.html(lang=lang):

def head(airium, title=metadata.project_name):
    a = airium
    with a.head():
        a.meta(charset='UTF-8')
        a.title(_t=str(title))
        a.meta(content='width=device-width,initial-scale=1', name='viewport')
        a.meta(content='', name='description')
        a.link(href='https://cdn.jsdelivr.net/npm/modern-normalize@v2.0.0/modern-normalize.min.css', rel='stylesheet')
        a.link(crossorigin='anonymous', href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css', rel='stylesheet')
        a.link(href='favicon.png', rel='icon')
        a.meta(content='#00a3d7', name='theme-color')
        a.meta(content='', property='og:title')
        a.meta(content='', property='og:description')
        a.meta(content='', property='og:image')
        a.meta(content='', name='twitter:card')
        a.meta(content='', name='twitter:site')
        a.meta(content='', name='twitter:title')
        a.meta(content='', name='twitter:description')
        a.meta(content='', name='twitter:image')
        a.script(crossorigin='anonymous', src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js')

def topbar(airium):
    a = airium
    with a.nav(klass='navbar navbar-expand-lg bg-body-tertiary'):
        with a.div(klass='container-fluid'):
            a.a(klass='navbar-brand', href='#', _t='Navbar')
            with a.button(klass='navbar-toggler', type='button', **{'aria-controls': 'navbarNavDropdown',
             'aria-expanded': 'false',
             'aria-label': 'Toggle navigation',
             'data-bs-target': '#navbarNavDropdown',
             'data-bs-toggle': 'collapse'}):
                a.span(klass='navbar-toggler-icon')
            with a.div(klass='collapse navbar-collapse', id='navbarNavDropdown'):
                with a.ul(klass='navbar-nav'):
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link active', href='#', **{'aria-current': 'page'}, _t='Home')
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link', href='#', _t='Features')
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link', href='#', _t='Pricing')
                    with a.li(klass='nav-item dropdown'):
                        with a.a(klass='nav-link dropdown-toggle', href='#', role='button', **{'aria-expanded': 'false', 'data-bs-toggle': 'dropdown'}):
                            a('Dropdown link')
                        with a.ul(klass='dropdown-menu'):
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Action')
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Another action')
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Something else here')

def footer(airium):
    with a.footer():
        with a.small():
            a('©')
            with a.script():
                a('document.write(new Date().getFullYear())')
            a(metadata.project_name+'. All Rights Reserved.')

