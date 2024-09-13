# Django Starter

How to use the django-starter:

- Clone the repo to a temp directory
- Rename the directory to the new project
- Move the entire directory to where you work
- `cd` into the directory
	- `rm -rf .git`
	- `rm README.md`
    - Update "starter" in ./bin/initialize-db script
    - Update .env.template to match
	- `git init`
	- `git add .`
	- `git commit -am "initial commit"`
- Create a repo on GitHub matching your project name
- Follow the "...or push and existing repository"
	- `git remote add origin git@github.com:username/project-name.git`
	- `git branch -M main`
	- `git push -u origin main`
- Create a README.md with how to set up a development environment
- Include
	- commands to run
	- databases to set up locally
	- etc
- To quickly bootstrap an environment with Python3.12, from the project directory run:
    - `./dev/initialize-env`
