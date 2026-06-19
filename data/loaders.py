import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_sample_market() -> dict:
    with (BASE_DIR / "sample_market.json").open() as fh:
        return json.load(fh)
