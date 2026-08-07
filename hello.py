"""Which Python is running this file?

Run it two ways and compare the output:

    python hello.py
    uv run python hello.py

The second always uses this project's environment. The first uses whatever your
computer finds first, which may be a different Python, or none at all.
"""

import sys

print("Version:", sys.version.split()[0])
print("Path:   ", sys.executable)
