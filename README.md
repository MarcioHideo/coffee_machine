# Coffee Machine Project

## Summary
This project is designed to simulate the functionality of a coffee machine. It includes features for selecting coffee types, managing ingredients, and payment by coins.

Additionally, this is only for educational purposes to highlight the core features of creating a new project.

## Creating a Git Repository
To create a new repository, follow these instructions:
1. `git init` to initialize Git.
2. `touch README.md` to create the README.md file as default.
3. `git add .` to add the files you want to commit to the repository.
4. `git commit -m "message"` to write down any message for the commits.
5. `git remote add origin https://github.com/your-username/your-repo-name.git` after creating the repository on the website, copy the Git HTTPS URL.
6. `git push -u origin main` to push the commits you made, or use `git pull origin main --rebase` to pull the remote changes.

### Extras for Git
If you have files or folders you do not want to commit, create a `.gitignore` file and specify the paths to exclude from the repository:
1. `touch .gitignore` to create the file.
2. Inside the file, write the paths of the files or folders you want to exclude, such as `venv/`.
3. Save the changes.

Note: The `.gitignore` file ensures that specified files or folders are ignored by Git during commits and pushes.

## Creating a Virtual Environment
A virtual environment is a key feature to create an isolated Python environment with its own independent set of Python packages, avoiding conflicts. Follow these instructions to create one:
1. `which -a python` to see all available Python installations on your system.
2. `/usr/local/bin/python3 -m venv venv` to create the virtual environment with the name 'venv' (you can choose any name, but 'venv' is commonly used by developers).
3. `source venv/bin/activate` to activate your new environment.

And that's it! You can now use your own virtual environment. Whenever you want to deactivate it, simply type `deactivate`.

<!-- Add detailed sections later -->
