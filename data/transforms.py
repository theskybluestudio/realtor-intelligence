SEGMENT_COLORS = {
    "full": "#2dd4bf",
    "s200": "#60a5fa",
    "s500": "#f59e0b",
    "s1m": "#818cf8",
    "s2m": "#f87171",
}


def series_to_rows(quarters: list[str], values: list[float], label: str) -> list[dict]:
    return [
        {"quarter": quarter, "value": value, "series": label}
        for quarter, value in zip(quarters, values)
    ]


def distribution_to_rows(items: list[dict]) -> list[dict]:
    return [{"label": item["label"], "value": item["pct"]} for item in items]


def segment_comparison_rows(data: dict, key: str, use_range: bool = False) -> list[dict]:
    rows = []
    for segment in data["segments"]:
        label = segment["range"] if use_range else segment["label"]
        rows.extend(series_to_rows(data["quarters"], segment["series"][key], label))
    return rows
