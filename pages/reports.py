import streamlit as st

from components.sections import render_section_header


def render(data: dict) -> None:
    render_section_header("Reports & Export", "📄")
    cols = st.columns(2)
    for idx, report in enumerate(data["reports"]):
        with cols[idx % 2]:
            button_class = "mesh-report-button-primary" if report.get("primary") else "mesh-report-button-secondary"
            st.markdown(
                f"""
                <div class='mesh-report-card'>
                  <div class='mesh-report-title'>{report['icon']} {report['title']}</div>
                  <div class='mesh-report-desc'>{report['desc']}</div>
                  <div class='mesh-report-button {button_class}'>{report['button']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
