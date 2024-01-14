

project_name = 'The Touch Grass Movement'

founders = {'charles shelby': {'email': 'charles.s.strauss@utah.edu', 'phone':'+1 505 309 5360'}}

contact_email = founders['charles shelby']['email']
contact_phone = founders['charles shelby']['phone']

import git

git_repo = git.Repo(search_parent_directories=True)
git_hash_sha = git_repo.head.object.hexsha # shortcut to the version so bugs can be traced to changes

basic_idea = f'What if Instagram, Facebook, Twitter, etc. all had a blackout month? {project_name} is a social experiment dedicated to spreading this idea. The official challenge starts on February 4 (the anniversary of Facebook\'s inception). Users\' accounts are tracked. They lose when they open a social media app.'


