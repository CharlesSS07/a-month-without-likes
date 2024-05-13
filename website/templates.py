
import metadata

import website.html

def html(airium, lang='en'):
    a = airium
    a('<!DOCTYPE html>')
    return a.html(lang=lang)

def head(airium, title=metadata.project_name, extension=None):
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
        a.script(crossorigin='anonymous', src='https://code.jquery.com/jquery-3.7.1.min.js')
        a.script(crossorigin='anonymous', src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js')
        if callable(extension):
            extension(a)

def topbar(airium):
    a = airium
    with a.nav(klass='navbar navbar-expand-lg bg-body-tertiary'):
        with a.div(klass='container-fluid'):
            a.a(klass='navbar-brand', href='/static/index.html', _t=metadata.project_name)
            with a.button(klass='navbar-toggler', type='button', **{'aria-controls': 'navbarNavDropdown',
             'aria-expanded': 'false',
             'aria-label': 'Toggle navigation',
             'data-bs-target': '#navbarNavDropdown',
             'data-bs-toggle': 'collapse'}):
                a.span(klass='navbar-toggler-icon')
            with a.div(klass='collapse navbar-collapse', id='navbarNavDropdown'):
                with a.ul(klass='navbar-nav'):
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link', href='/static/login.html', **{'aria-current': 'page'}, _t='Sign Up')
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link', href='#', _t='Tune In')
                    with a.li(klass='nav-item'):
                        a.a(klass='nav-link', href='#', _t='Log Out')
                    with a.li(klass='nav-item dropdown'):
                        with a.a(klass='nav-link dropdown-toggle', href='#', role='button', **{'aria-expanded': 'false', 'data-bs-toggle': 'dropdown'}):
                            a('30 Days.')
                        with a.ul(klass='dropdown-menu'):
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Action')
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Another action')
                            with a.li():
                                a.a(klass='dropdown-item', href='#', _t='Something else here')

def footer(airium):
    a = airium
    with a.footer():
        with a.small():
            a('©')
            with a.script():
                a('document.write(new Date().getFullYear())')
            a(metadata.project_name+'. All Rights Reserved.')

def firebase(airium):
    a = airium
    with a.script(type='module'):
        a('''
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCwPMeRKfWGfHJi7zvOl3mOdtTMrjuneZY",
    authDomain: "one-month-challenge-website.firebaseapp.com",
    projectId: "one-month-challenge-website",
    storageBucket: "one-month-challenge-website.appspot.com",
    messagingSenderId: "11192636690",
    appId: "1:11192636690:web:c981c1a6ed04250e724fcb",
    measurementId: "G-3QJX2CF436"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);''')
