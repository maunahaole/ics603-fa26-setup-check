# Checking your setup

Run these in a terminal opened in this project folder. In VS Code that is
*Terminal → New Terminal*, which already starts in the right place.

```bash
uv --version
uv run python --version    # expect Python 3.13.x
uv run python hello.py
git --version
```

If all four work, `uv`, Python, and Git are installed. Whether VS Code itself is
set up correctly is not covered by these commands — steps 5 and 8 of the
[README](README.md) are what check that.

## Problems that come up most often

| What you see | Likely cause | What to try |
|---|---|---|
| `uv: command not found`, or on Windows `The term 'uv' is not recognized...` | Your terminal has not picked up the updated PATH. | Close the terminal and open a new one. If a new terminal does not help, `uv` is probably not installed — run the installer from the setup handout again. |
| `python` opens the Microsoft Store | Windows is using its Store alias instead of a real Python. | Use `uv run python`. This is expected, not a failure. |
| `python: command not found` on macOS | macOS provides `python3`, not `python`. | Use `uv run python`. This is expected too, and it is the point of step 4. |
| `uv run python --version` reports something other than 3.13 | The project picked a different interpreter than `.python-version` asks for. | Run `uv python install 3.13`, then `uv sync` again. |
| **Python: Select Interpreter** is not in the command palette | The Microsoft Python extension is not installed. | Install it from the Extensions view, then reload VS Code. |
| VS Code offers no interpreter inside `.venv` | `.venv` does not exist yet, or VS Code has not noticed it. | Run `uv sync` first, then reload VS Code and select the interpreter again. |
| `python hello.py` and `uv run python hello.py` print the *same* path | You are in a VS Code terminal and VS Code has activated `.venv` for you. | Expected after step 5. To see the difference, use a terminal you opened outside VS Code. |
| The Source Control panel says Git is not found, or `git --version` fails | Git is not installed, or VS Code was already open when you installed it. | Install Git as described in the setup handout, then quit and reopen VS Code. |
| **Git: Clone** lists no repositories | VS Code is not signed in to GitHub. | Click the **Accounts** icon at the bottom of the left sidebar and sign in with GitHub. |
| The push fails with a permissions error | You cloned the course template instead of your own copy. | Use **Use this template** to make your own copy, then clone that. |

## Asking for help

Copy this into Slack and fill it in. Exact text beats a description of the text:
paraphrasing an error message removes the part that identifies it.

```text
Operating system:
uv --version:
uv run python --version:
git --version:

What I ran:

What I expected:

The exact error, copied and pasted:

What I already tried:
```

If the problem is visual — the interpreter picker, the Source Control panel, a
VS Code dialog — attach a screenshot too.
