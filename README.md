# ICS 603 setup check

A throwaway project for the session 2 setup check. It exists so you can prove, in
a few minutes, that four things work together: `uv`, Python, VS Code, and GitHub
Desktop.

You will not build anything on top of this. Delete it whenever you like.

## Get your own copy

Click **Use this template** → **Create a new repository** at the top of this
page. Set the owner to your own account, and leave the repository **Public** so
the URL you share at the end is one the instructor can open.

Do not clone this repository directly. You do not have permission to push to it,
so the last step would fail.

`me.md` is the only file you edit, and your copy is public. Put nothing in it
that you would not post publicly.

## The steps

1. **Use this template** to create your own copy.

2. **Clone it** in GitHub Desktop: *File → Clone repository*, then open the
   **GitHub.com** tab. Your new copy is in the list, under your own account.

3. **Create the environment.** Open a terminal in the folder and run:

   ```bash
   uv sync
   ```

   A `.venv` folder appears. This project has no dependencies, so nothing is
   downloaded and it finishes almost at once — unless Python 3.13 is missing
   from your machine, in which case `uv` fetches it first. That download is
   about 24 MB and happens only once.

4. **See which Python you get by default.** Do this **before** the next step,
   and do it in a terminal you opened yourself — Terminal on macOS, PowerShell
   on Windows — not inside VS Code. The next step changes the answer, which is
   the point. Run both:

   ```bash
   python hello.py
   uv run python hello.py
   ```

   The second prints a path inside `.venv`. The first prints something else, or
   fails. On macOS it usually fails with `python: command not found`, because
   macOS has no command named `python`. On Windows it may open the Microsoft
   Store. All three outcomes are correct results — write down which one you got.

5. **Point VS Code at the project.** Open the folder in VS Code, press
   `Ctrl`/`Cmd` + `Shift` + `P`, run **Python: Select Interpreter**, and choose
   the interpreter inside `.venv`. This needs the Microsoft Python extension,
   which the setup handout had you install.

   Now open a terminal *inside* VS Code — *Terminal → New Terminal* — and run
   `python hello.py` again. This time it prints the `.venv` path, the same one
   `uv run python` printed. Selecting the interpreter changed what `python`
   means in that terminal. That is exactly what the setting does.

6. **Add a dependency.**

   ```bash
   uv add rich
   uv run python -c "import rich; print('it works')"
   ```

   Now look at `pyproject.toml` and `uv.lock`. Both changed. `uv.lock` went from
   one entry to five, because `rich` depends on three other packages of its own.

7. **Edit `me.md`** and fill in the three blanks.

8. **Commit, push, and share.** In GitHub Desktop, read the changes, write a
   short message such as `Add setup notes`, click **Commit to main**, then
   **Push origin**. Refresh your repository on github.com — your change is there.
   Paste that repository URL in the setup channel on Slack.

## If something fails

See [`CHECK.md`](CHECK.md). It has the commands for checking your setup, the
problems that come up most often, and a template for asking for help in a way
that gets answered quickly.
