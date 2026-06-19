from pathlib import Path

import streamlit as st


def inject_css(base_dir: Path) -> None:
    css_path = base_dir / 'assets' / 'styles.css'
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
