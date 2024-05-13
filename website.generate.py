#!/usr/bin/env python

import metadata

import website

from airium import Airium
a = Airium()

import config
out_dir = config.website_static

import shutil
import os
if os.path.exists(out_dir):
    shutil.rmtree(out_dir)
os.makedirs(out_dir)

def stash_webpage(html, output_file):
    print(output_file.as_posix())
    with open(output_file.as_posix(), 'w') as f:
        f.write(html)

a = Airium()
import website.pages.main
stash_webpage(website.pages.main.generate(a), out_dir / 'index.html')

a = Airium()
import website.pages.login
stash_webpage(website.pages.login.generate(a), out_dir / 'login.html')
