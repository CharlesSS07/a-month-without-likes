#!/usr/bin/env python

import metadata

import website

from airium import Airium

a = Airium()

out_dir = 'gen/static'

import shutil
import os
if os.path.exists(out_dir)
    shutil.rmtree(out_dir)
os.makedirs(out_dir)

website.generate(a, glob.glob('./website/pages/*', 'gen/static')
