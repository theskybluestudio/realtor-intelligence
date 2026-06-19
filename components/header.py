import streamlit as st


BADGE_TONE_CLASS = {
    "green": "mesh-badge-green",
    "teal": "mesh-badge-teal",
    "amber": "mesh-badge-amber",
    "red": "mesh-badge-red",
    "blue": "mesh-badge-blue",
}


def render_header(market: dict) -> None:
    meta_html = "".join(
        f"<span class='mesh-pill'><span class='mesh-pill-dot'></span>{label}: {value}</span>"
        for label, value in market.get("meta", [])
    )
    badge_class = BADGE_TONE_CLASS.get(market.get("condition_tone", "green"), "mesh-badge-green")
    st.markdown(
        f"""
        <div class='mesh-header'>
          <div>
            <div class='mesh-header-kicker'>{market['title']}</div>
            <div class='mesh-header-title'>{market['location']}</div>
            <div class='mesh-header-subtitle'>{market['subtitle']}</div>
            <div class='mesh-pill-row'>{meta_html}</div>
          </div>
          <div class='mesh-header-side'>
            <div class='mesh-badge {badge_class}'>{market['condition_label']}</div>
            <div class='mesh-header-updated'>Last updated: {market['last_updated']} — {market['period']}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
