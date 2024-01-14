

import importlib.util

import glob

from pathlib import Path

def generate_webpages(airium, page_list, output_dir):
    
    for page in page_list:
        
        if type(page)==str:
            spec = importlib.util.spec_from_file_location("pagemodule", page)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            html = foo.html(airium)
        
            with open(Path(output_dir)/foo.page_path, 'w') as f:
                f.write(html)
