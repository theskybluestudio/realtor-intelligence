import streamlit as st

from components.charts import render_bar_chart, render_gauge, render_line_chart
from components.kpi_cards import render_kpi_grid
from components.sections import render_alert, render_section_header
from data.transforms import SEGMENT_COLORS, distribution_to_rows, series_to_rows


PRICE_KPIS = [
    {"label": "Median Sale Price", "key": "medPrice", "badge": "yoy", "badge_type": "up", "note": "vs $505K (2023)", "accent": "#34d399"},
    {"label": "Average Sale Price", "key": "avgPrice", "badge": "▲ 9.8% YoY", "badge_type": "up", "note": "vs $584K (2023)", "accent": "#2dd4bf"},
    {"label": "Median Price / Sq Ft", "key": "ppsf", "badge": "▲ 7.5% YoY", "badge_type": "up", "note": "Avg: $241/sq ft", "accent": "#f59e0b"},
    {"label": "List-to-Sale Ratio", "key": "lsr", "badge": "Rising", "badge_type": "rising", "note": "+0.9pp YoY", "accent": "#60a5fa"},
    {"label": "Sold Above List", "key": "competitive", "badge": "▲ 4pp YoY", "badge_type": "up", "note": "Competitive offer rate", "accent": "#34d399"},
    {"label": "3-Year Price Growth", "key": "sold3yr", "badge": "Rising", "badge_type": "rising", "note": "Q1 2023 – Q1 2026", "accent": "#f59e0b"},
]

DOM_KPIS = [
    {"label": "Avg Days on Market", "key": "dom", "badge": "Cooling ▲", "badge_type": "cooling", "note": "+5 days YoY", "accent": "#2dd4bf"},
    {"label": "Median Days on Market", "key": "medDom", "badge": "Stable", "badge_type": "flat", "note": "vs 17 days (2023)", "accent": "#60a5fa"},
    {"label": "Avg Days to Close", "key": "dtc", "badge": "Stable", "badge_type": "flat", "note": "Post-offer to funding", "accent": "#f59e0b"},
    {"label": "Total Time to Sale", "key": "tts", "badge": "▲ 5 days YoY", "badge_type": "up", "note": "Listing → close", "accent": "#34d399"},
    {"label": "Expired / Withdrawn", "key": "expiredPct", "badge": "▲ 1.4pp YoY", "badge_type": "down", "note": "of all listings", "accent": "#f87171"},
]

SUPPLY_KPIS = [
    {"label": "Active Listings", "key": "active", "badge": "▼ 18% YoY", "badge_type": "down", "note": "vs 1,034 (Q1 2025)", "accent": "#f87171"},
    {"label": "Months of Supply", "key": "supply", "badge": "Seller's Zone", "badge_type": "cooling", "note": "Below 3-month threshold", "accent": "#f87171"},
    {"label": "New Listings (90d)", "key": "newList", "badge": "Stable", "badge_type": "flat", "note": "+2.1% QoQ", "accent": "#f59e0b"},
    {"label": "Absorption Rate", "key": "absorb", "badge": "▲ 8pp YoY", "badge_type": "up", "note": "Per month", "accent": "#2dd4bf"},
    {"label": "Cash Sale %", "key": "cash", "badge": "▲ 1.8pp YoY", "badge_type": "up", "note": "No-financing transactions", "accent": "#34d399"},
]


def _metric_items(kpis: dict, specs: list[dict]) -> list[dict]:
    items = []
    for spec in specs:
        item = dict(spec)
        item["value"] = kpis[spec["key"]]
        if spec.get("badge") == "yoy":
            item["badge"] = kpis["yoy"]
        items.append(item)
    return items


def _card_start(title: str, subtitle: str) -> None:
    st.markdown(f"<div class='mesh-chart-card'><div class='mesh-card-title'>{title}</div><div class='mesh-card-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def _card_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render(data: dict) -> None:
    seg = data["segments"][0]
    kpis = seg["kpis"]

    render_section_header("Market Pricing Metrics", "💰")
    render_kpi_grid(_metric_items(kpis, PRICE_KPIS), columns=3)

    price_rows = []
    price_rows.extend(series_to_rows(data["quarters"], seg["series"]["median_price"], "Median"))
    price_rows.extend(series_to_rows(data["quarters"], seg["series"]["average_price"], "Average"))
    dist_rows = distribution_to_rows(data["distribution"])
    left, right = st.columns(2)
    with left:
        _card_start("Median & Average Price — 3 Year Trend", "Quarterly, Q1 2023 – Q1 2026 · The Woodlands, TX")
        render_line_chart(price_rows, "", "Price (K)", {"Median": SEGMENT_COLORS["full"], "Average": "#f59e0b"})
        _card_end()
    with right:
        _card_start("Sale Price Distribution", "All closed transactions, Q1 2026 (YTD)")
        render_bar_chart(dist_rows, "", "Share of sales (%)")
        _card_end()

    render_section_header("Time-on-Market Metrics", "⏱")
    render_kpi_grid(_metric_items(kpis, DOM_KPIS), columns=5)

    dom_rows = []
    dom_rows.extend(series_to_rows(data["quarters"], seg["series"]["dom_avg"], "Avg DOM"))
    dom_rows.extend(series_to_rows(data["quarters"], seg["series"]["dom_med"], "Median DOM"))
    inventory_rows = []
    inventory_rows.extend(series_to_rows(data["quarters"], seg["series"]["inventory"], "Active Listings"))
    inventory_rows.extend(series_to_rows(data["quarters"], [v * 100 for v in seg["series"]["supply"]], "Months Supply x100"))
    left, right = st.columns(2)
    with left:
        _card_start("Days on Market Trend", "Average and median DOM, quarterly")
        render_line_chart(dom_rows, "", "Days", {"Avg DOM": "#818cf8", "Median DOM": "#2dd4bf"})
        _card_end()
    with right:
        _card_start("Inventory Trend", "Active listings with months of supply overlay")
        render_line_chart(inventory_rows, "", "Index", {"Active Listings": "#f59e0b", "Months Supply x100": "#f87171"})
        _card_end()

    render_section_header("Inventory & Supply", "📦")
    render_alert(f"<strong>Low Inventory Alert:</strong> Months of supply is {kpis['supply']} — below the 3-month threshold. Inventory is critically constrained.")
    render_kpi_grid(_metric_items(kpis, SUPPLY_KPIS), columns=5)

    render_section_header("Market Condition & Intelligence", "📊")
    left, right = st.columns([1, 1.15])
    with left:
        _card_start("Market Heat Score", "Composite demand and supply balance")
        render_gauge(kpis["heatScore"], "Heat Score")
        st.markdown(
            f"<div class='mesh-card-subtitle'><strong style='color:#34d399'>🔥 {kpis['cond']}</strong><br>Months of supply under 2, DOM under 30 days, and {kpis['competitive']} of homes closing above list price signal a strong seller advantage across The Woodlands.</div>",
            unsafe_allow_html=True,
        )
        _card_end()
    with right:
        summary_rows = [
            ("Market Condition", kpis["cond"]),
            ("Price Trend", "Rising ▲"),
            ("Inventory Trend", "Tightening ▼"),
            ("DOM Trend", "Stable →"),
            ("Competitive Offer Rate", f"{kpis['competitive']} sold above ask"),
            ("Cash Sale %", kpis["cash"]),
            ("List-to-Sale Ratio", kpis["lsr"]),
            ("Market Heat Score", f"{kpis['heatScore']} / 100"),
        ]
        rows_html = "".join(
            f"<div class='mesh-summary-row'><span class='mesh-summary-label'>{label}</span><span class='mesh-summary-value'>{value}</span></div>"
            for label, value in summary_rows
        )
        st.markdown(
            f"<div class='mesh-summary-card'><div class='mesh-card-title'>Market Indicators Summary</div><div class='mesh-card-subtitle'>Quick read across demand, pricing, and inventory pressure.</div>{rows_html}</div>",
            unsafe_allow_html=True,
        )
