import streamlit as st

from components.charts import render_line_chart
from components.kpi_cards import render_kpi_grid
from components.sections import render_alert, render_section_header
from data.transforms import SEGMENT_COLORS, series_to_rows


SEGMENT_METRICS = [
    {"label": "Median Sale Price", "key": "medPrice", "badge": "yoy", "badge_type": "up"},
    {"label": "Average Sale Price", "key": "avgPrice", "badge": "▲ YoY", "badge_type": "up"},
    {"label": "Price / Sq Ft", "key": "ppsf", "badge": "▲ YoY", "badge_type": "up"},
    {"label": "List-to-Sale Ratio", "key": "lsr", "badge": "Stable", "badge_type": "flat"},
    {"label": "Avg Days on Market", "key": "dom", "badge": "Stable", "badge_type": "flat"},
    {"label": "Median DOM", "key": "medDom", "badge": "Stable", "badge_type": "flat"},
    {"label": "Active Listings", "key": "active", "badge": "▼ YoY", "badge_type": "down"},
    {"label": "Months of Supply", "key": "supply", "badge": "zone", "badge_type": "stable"},
    {"label": "Absorption Rate", "key": "absorb", "badge": "▲ YoY", "badge_type": "up"},
    {"label": "Cash Sale %", "key": "cash", "badge": "▲ YoY", "badge_type": "up"},
    {"label": "Competitive Offer Rate", "key": "competitive", "badge": "▲ YoY", "badge_type": "up"},
    {"label": "Heat Score", "key": "heatScore", "badge": "heat", "badge_type": "info"},
]

ACCENTS = ["#2dd4bf", "#60a5fa", "#f59e0b", "#818cf8", "#f87171", "#34d399"]


def _metric_items(segment: dict) -> list[dict]:
    items = []
    kpis = segment["kpis"]
    for idx, spec in enumerate(SEGMENT_METRICS):
        item = dict(spec)
        value = kpis[spec["key"]]
        if spec["key"] == "heatScore":
            value = f"{value} / 100"
        item["value"] = value
        if spec["badge"] == "yoy":
            item["badge"] = kpis["yoy"]
        elif spec["badge"] == "zone":
            supply_num = float(kpis["supply"].split()[0])
            item["badge"] = "Seller's Zone" if supply_num < 3 else "Balanced" if supply_num < 6 else "Buyer's Zone"
            item["badge_type"] = "cooling" if supply_num < 3 else "stable"
        elif spec["badge"] == "heat":
            score = kpis["heatScore"]
            item["badge"] = "Hot" if score > 70 else "Moderate" if score > 55 else "Cool"
            item["badge_type"] = "rising" if score > 70 else "stable"
        item["accent"] = ACCENTS[idx % len(ACCENTS)]
        items.append(item)
    return items


def _card_start(title: str, subtitle: str) -> None:
    st.markdown(f"<div class='mesh-chart-card'><div class='mesh-card-title'>{title}</div><div class='mesh-card-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def _card_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render(data: dict, segment: dict) -> None:
    if segment.get("low_volume"):
        render_alert("⚠️ <strong>Low Volume Warning:</strong> This segment recorded fewer than 50 transactions in Q1 2026 — metrics may have reduced statistical reliability.", tone="amber")

    render_section_header(f"{segment['range']} Segment · Pricing & Metrics", "💰")
    render_kpi_grid(_metric_items(segment), columns=4)

    label = segment["range"]
    color = SEGMENT_COLORS[segment["id"]]
    left, right = st.columns(2)
    with left:
        _card_start(f"Median Price Trend — {label}", "Quarterly, Q1 2023 – Q1 2026")
        render_line_chart(series_to_rows(data["quarters"], segment["series"]["median_price"], label), "", "Price (K)", {label: color})
        _card_end()
    with right:
        rows = []
        rows.extend(series_to_rows(data["quarters"], segment["series"]["dom_avg"], "Avg DOM"))
        rows.extend(series_to_rows(data["quarters"], segment["series"]["dom_med"], "Median DOM"))
        _card_start(f"Days on Market — {label}", "Average and median DOM, quarterly")
        render_line_chart(rows, "", "Days", {"Avg DOM": color, "Median DOM": "#2dd4bf"})
        _card_end()

    left, right = st.columns(2)
    with left:
        _card_start(f"Inventory Trend — {label}", "Active listings, quarterly")
        render_line_chart(series_to_rows(data["quarters"], segment["series"]["inventory"], "Active Listings"), "", "Listings", {"Active Listings": "#f59e0b"})
        _card_end()
    with right:
        _card_start(f"Months of Supply — {label}", "Quarterly supply level")
        render_line_chart(series_to_rows(data["quarters"], segment["series"]["supply"], "Months Supply"), "", "Months", {"Months Supply": color})
        _card_end()
