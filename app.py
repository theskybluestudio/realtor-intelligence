from pathlib import Path

import streamlit as st

from components.header import render_header
from components.layout import inject_css
from components.segment_strip import render_segment_strip
from components.sections import render_footer
from data.loaders import load_sample_market
from pages import comparison, full_market, reports, segment as segment_page
from utils.constants import TAB_DEFINITIONS
from utils.state import init_state


BASE_DIR = Path(__file__).resolve().parent


st.set_page_config(
    page_title="Realtor Intelligence",
    page_icon="🏡",
    layout="wide",
)


def main() -> None:
    inject_css(BASE_DIR)
    init_state()
    data = load_sample_market()

    render_header(data["market"])
    render_segment_strip(data["segments"])

    tabs = st.tabs([label for _, label in TAB_DEFINITIONS])

    with tabs[0]:
        full_market.render(data)
    with tabs[1]:
        segment_page.render(data, data["segments"][1])
    with tabs[2]:
        segment_page.render(data, data["segments"][2])
    with tabs[3]:
        segment_page.render(data, data["segments"][3])
    with tabs[4]:
        segment_page.render(data, data["segments"][4])
    with tabs[5]:
        comparison.render(data)
    with tabs[6]:
        reports.render(data)

    render_footer(data["market"]["footer"])


if __name__ == "__main__":
    main()
