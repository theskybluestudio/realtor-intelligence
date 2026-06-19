import html

import streamlit as st


BADGE_CLASS_MAP = {
    "up": "green",
    "down": "red",
    "flat": "blue",
    "rising": "green",
    "cooling": "red",
    "stable": "amber",
    "info": "purple",
    "hot": "amber",
}


def render_kpi_grid(items: list[dict], columns: int = 3) -> None:
    for start in range(0, len(items), columns):
        row = st.columns(columns)
        for col, item in zip(row, items[start : start + columns]):
            with col:
                badge = item.get("badge")
                badge_tone = BADGE_CLASS_MAP.get(item.get("badge_type", "flat"), "blue")
                badge_html = ""
                if badge:
                    badge_html = f"<span class='mesh-badge mesh-badge-{badge_tone}'>{html.escape(str(badge))}</span>"
                note = html.escape(str(item.get("note", "")))
                accent = item.get("accent", "#2dd4bf")
                st.markdown(
                    f"""
                    <div class='mesh-card mesh-kpi-card' style='--accent:{accent}'>
                      <div class='mesh-kpi-label'>{html.escape(str(item['label']))}</div>
                      <div class='mesh-kpi-value'>{html.escape(str(item['value']))}</div>
                      <div class='mesh-kpi-meta'>{badge_html}</div>
                      <div class='mesh-kpi-note'>{note}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
