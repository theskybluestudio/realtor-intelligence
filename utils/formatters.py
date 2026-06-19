def format_currency_k(value: float | int) -> str:
    return f"${value:,.0f}K"


def format_percent(value: float | int) -> str:
    return f"{value}%"


def format_days(value: float | int) -> str:
    return f"{value}d"
