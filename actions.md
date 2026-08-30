# Step by step actions

### Fork
- Fork repo on github
- git clone (insert HTTPS)
- cd directory name
- git remote add upstream (insert HTTPS)
- git remote -v
- gh repo set-default
    - pick your fork
- git checkout -b (new branch name)
- git push -u origin (new branch name)

### Assignment: 1.1.1 After-Class Git Walkthrough

#### Resources:
- https://github.com/ics-professional-program/ics603-fa26-materials/tree/main/1.1-Python-Environment-Setup

#### My Work:
- CMD + SHIFT + P
    - Python: Select Interpreter
    - Enter Interpreter Path:
        - /Users/dominicbarrale/UH_Manoa/ICS_603/ics603-fa26-setup-check/.venv/bin/python 
            - absolute path
- CMD + SHIFT + P
    - Developer: Reload Window

- uv add rich
- uv sync
- hello.py:
    - from rich import print
    - print("[bold cyan]Hello hello-ics603![/bold cyan]")
- uv sync
- python hello.py
    - doesnt work not using venv
- uv run python hello.py
    - works uses venv

- update me.md


### Push version to Github
- git status
- git add .
- git commit -m "ICS 603 setup check"
- git push

### Merge branch to main from Github
- gh pr create
- gh pr merge
- git checkout main
    - ensures you are on main branch after pr merge
- git branch -r
- git fetch --prune
    - downloads the latest branch info from GitHub and deletes your local "remembered" copies of any remote branches that no longer exist there — like origin/dev, which you deleted during the merge but your clone still lists
- git branch -r

### Assignment: After-Class Jupyter Walkthrough

#### Resources:
- https://github.com/ics-professional-program/ics603-fa26-materials/tree/main/1.2-Jupyter-Notebooks-Workflow

#### My Work:
- at project root:
    - touch main.ipynb
    - Select Kernel
        - Python Environments
            - setup-check venv
        
- touch main.ipynb
    - select project kernel
    - MD 
    - confirm kernel envir
    - observe kernel state
    - restart and run all

### Push version to Github
- git status
- git add .
- git commit -m "ICS 603 setup check"
- git push