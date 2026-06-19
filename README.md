# realtor-intelligence

Streamlit application for realtor intelligence.

## Python version

This project targets **Python 3.12** and uses a project-local virtual environment at `.venv/`.

## Setup

```bash
cd _topics/realtor-intelligence/application
/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
source .venv/bin/activate
streamlit run app.py
```

## Structure

- `app.py` — main Streamlit entrypoint
- `components/` — reusable UI pieces
- `data/` — sample dataset and loading helpers
- `pages/` — tab content renderers
- `utils/` — formatting, constants, session state helpers
- `assets/` — CSS and static assets
- `docs/` — roadmap and architecture notes
- `BLUEPRINT.md` — current implementation blueprint
