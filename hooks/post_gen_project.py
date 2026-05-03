import os
import shutil


# Delete `.github` folder if not using GitHub Actions
if not {{ cookiecutter.automatic_docs_to_pages }}:
    actions_path = os.path.join(os.getcwd(), '.github')
    if os.path.exists(actions_path):
        shutil.rmtree(actions_path)
