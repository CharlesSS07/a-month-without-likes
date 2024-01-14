#!/usr/bin/env python

import metadata

with open('gen/metadata.md', 'w') as md:
    md.write(f'''---
project_name:{metadata.project_name}
git_hash_sha:{metadata.git_hash_sha}
basic_ide:{metadata.basic_idea}
---''')
    
