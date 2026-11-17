# Dev Workspace

**WebMagic Informatica · dabeer.ai**

Your ready-made coding workspace for every WebMagic Informatica and dabeer.ai course.
It runs in your browser with GitHub Codespaces, so you don't need to install anything on your computer.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/webmagicinformatica/dev-workspace)

## Get started

1. Sign in to GitHub with **your own** account (a free account is fine).
2. Click **Use this template** → **Create a new repository**. Name it (e.g. `my-ai-labs`), keep it **Private**, and create it.
3. In your new repo, click the green **Code** button → **Codespaces** → **Create codespace on main**, and wait a minute or two while it sets up.
4. In the terminal at the bottom, run:

   ```bash
   python hello.py
   ```

   You should see your Python version and whether your API keys are set.

## What's installed

| Tool | What it's for |
| --- | --- |
| Python 3.12 | Running Python code |
| uv | Fast Python package and project manager (`uv pip install ...`, `uv run ...`) |
| Node.js (LTS) + npm | JavaScript tools and labs |
| GitHub CLI (`gh`) | Working with GitHub from the terminal |
| VS Code extensions | Python, Pylance, Jupyter notebooks, Markdown preview |

Some labs need extra tools (for example Docker). Those labs will tell you how to add them.

## Save your free hours

Your personal GitHub account gets a free monthly Codespaces allowance (about **60 hours** on this 2-core machine, plus **15 GB** of storage). A codespace uses hours while it's running, even if you're not typing. Storage counts even when it's stopped.

- **Stop it when you're done.** Go to [github.com/codespaces](https://github.com/codespaces), click **⋯** next to your codespace → **Stop codespace**. Closing the browser tab doesn't stop it straight away.
- **Use a short idle timeout.** Codespaces stop by themselves after 30 minutes without activity. You can make that shorter: [Settings → Codespaces](https://github.com/settings/codespaces) → **Default idle timeout** (for example 10 minutes).
- **Delete old codespaces.** Each one uses storage. On [github.com/codespaces](https://github.com/codespaces), click **⋯** → **Delete** on any you don't need. Push your work to GitHub first.
- **Keep the small machine.** This workspace uses the 2-core machine, the cheapest one. Bigger machines use your hours faster.

## Add API keys safely

Never put API keys in files, code or notebooks, and never commit them. Use **Codespaces secrets** instead.

Secrets are given to a codespace through its repository, so your codespace must belong to a repo in your account first. If you followed the steps above, it already does. (If you opened a codespace straight from the template or the badge, publish it once: **Source Control** panel → **Publish Branch**.)

1. Go to [Settings → Codespaces](https://github.com/settings/codespaces).
2. Under **Codespaces secrets**, click **New secret**.
3. Name it, for example `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, and paste the key as the value.
4. Under **Repository access**, choose your copy of this repo.
5. Click **Add secret**.
6. If your codespace is already open, stop it and start it again so it picks up the new secret.

Your key is now available as an environment variable. Check with `python hello.py`, which only says **yes** or **no** and never shows the key. In Python, read it like this:

```python
import os
api_key = os.environ["ANTHROPIC_API_KEY"]
```

If a lab uses a `.env` file, it's already listed in `.gitignore`, so Git won't upload it.

## Need help?

Courses and labs: [webmagicinformatica.com](https://webmagicinformatica.com) · YouTube: **dabeer.ai**

MIT licensed. See [LICENSE](LICENSE).
