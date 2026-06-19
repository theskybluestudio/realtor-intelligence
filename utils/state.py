import streamlit as st


def init_state(default_segment: str = "full") -> None:
    st.session_state.setdefault("active_segment", default_segment)
