"""Quick check that your workspace is ready.

Run it with:  python hello.py
"""
import os
import platform


def is_set(name: str) -> str:
    # Only says yes or no. Never prints the key itself.
    return "yes" if os.environ.get(name) else "no"


print("Hello from your WebMagic Informatica · dabeer.ai workspace!")
print(f"Python version: {platform.python_version()}")
for key in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY"):
    print(f"{key} set: {is_set(key)}")
