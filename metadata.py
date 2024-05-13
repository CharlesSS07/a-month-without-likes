

project_name = 'A Month Without Likes'

founders = {'charles shelby': {'email': 'charles.s.strauss@utah.edu', 'phone':'+1 505 309 5360'}}

contact_email = founders['charles shelby']['email']
contact_phone = founders['charles shelby']['phone']

import git

git_repo = git.Repo(search_parent_directories=True)
git_hash_sha = git_repo.head.object.hexsha # shortcut to the version so bugs can be traced to changes

slogan = 'Sign up, tune in, and log out.'

sales_pitch = f'How would society change if Instagram, Facebook, Twitter, etc. just stopped working? {project_name} is a movement dedicated to spreading this idea through a one-month no social media challenge. The official challenge starts on February 4th.'


