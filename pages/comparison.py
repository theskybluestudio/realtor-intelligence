import streamlit as st

from components.charts import render_line_chart
from components.sections import render_section_header
from data.transforms import SEGMENT_COLORS, segment_comparison_rows


def _card_start(title: str, subtitle: str) -> None:
    st.markdown(f"<div class='mesh-chart-card'><div class='mesh-card-title'>{title}</div><div class='mesh-card-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def _card_end() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render(data: dict) -> None:
    color_map = {
        segment["range"] if segment["id"] != "full" else segment["label"]: SEGMENT_COLORS[segment["id"]]
        for segment in data["segments"]
    }

    render_section_header("Cross-Segment Comparison", "↗")

    _card_start("Median Price — All Segments Overlay", "Quarterly trend, Q1 2023 – Q1 2026")
    render_line_chart(segment_comparison_rows(data, "median_price", use_range=True), "", "Price (K)", color_map)
    _card_end()

    _card_start("Days on Market — All Segments Overlay", "Average DOM trend across all price tiers")
    render_line_chart(segment_comparison_rows(data, "dom_avg", use_range=True), "", "Days", color_map)
    _card_end()

    _card_start("Months of Supply — All Segments", "Below 3mo = seller's market, above 6mo = buyer's market")
    render_line_chart(segment_comparison_rows(data, "supply", use_range=True), "", "Months", color_map)
    _card_end()
