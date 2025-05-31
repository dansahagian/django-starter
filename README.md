# Django Starter

## How to use the django-starter:

- Clone the repo to a temp directory
- Rename the directory to the new project
- Move the entire directory to where you work
- `cd` into the directory
	- `rm -rf .git`
	- `rm README.md`
    - Update "starter" in dev/initialize-db script
    - Update .env.template to match
    - Create a README.md with how to set up a development environment
      - Include
        - commands to run
        - databases to set up locally
        - etc
    - `git init`
    - `git add .`
    - `git commit -am "initial commit"`
- Create a repo on GitHub matching your project name
- Follow the "...or push and existing repository"
	- `git remote add origin git@github.com:username/project-name.git`
	- `git branch -M main`
	- `git push -u origin main`

## The starter uses uv. To quickly bootstrap an environment.
If you have used this setup guide before, you can jump to the final step to create your virtualenv
and install dependencies:

Install uv:
https://docs.astral.sh/uv/

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install `ruff` and `pre-commit`:
```shell
uv tool install ruff
uv tool install pre-commit
```

Make sure these are on your PATH:
```shell
export PATH=$PATH:~/.cargo/bin
export PATH=$PATH:~/.local/bin
```

Add this to your shell configuration to make running management commands much shorter:
```shell
alias uvm="uv run python manage.py"
```

Create the virtualenv and install dependencies:
```shell
dev/initialize-env
```
