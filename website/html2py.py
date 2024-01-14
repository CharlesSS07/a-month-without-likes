

from airium import from_html_to_airium

html = '''<footer>
    <small>© <script>document.write(new Date().getFullYear())</script> Your company name. All Rights Reserved.</small>
  </footer>'''

print(from_html_to_airium(html))
