import streamlit as st


def render_section_header(title: str, icon: str = "") -> None:
    icon_html = f"<span class='mesh-section-icon'>{icon}</span>" if icon else ""
    st.markdown(
        f"<div class='mesh-section-title'>{icon_html}<span>{title}</span><div class='mesh-section-rule'></div></div>",
        unsafe_allow_html=True,
    )


def render_alert(message: str, tone: str = "red") -> None:
    st.markdown(
        f"<div class='mesh-alert mesh-alert-{tone}'>{message}</div>",
        unsafe_allow_html=True,
    )


def render_footer(lines: list[str]) -> None:
    items = "".join(f"<div>{line}</div>" for line in lines)
    st.markdown(f"<div class='mesh-footer'>{items}</div>", unsafe_allow_html=True)
