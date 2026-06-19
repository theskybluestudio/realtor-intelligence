import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


PLOT_BG = "#111827"
GRID = "rgba(148,163,184,0.16)"
TEXT = "#e2e8f0"
MUTED = "#94a3b8"
SEGMENT_COLORS = ["#2dd4bf", "#60a5fa", "#f59e0b", "#818cf8", "#f87171"]


def _style_figure(fig: go.Figure, y_axis_title: str = "") -> go.Figure:
    fig.update_layout(
        paper_bgcolor=PLOT_BG,
        plot_bgcolor=PLOT_BG,
        font_color=TEXT,
        legend_title_text="",
        margin=dict(l=18, r=18, t=46, b=18),
        xaxis_title="",
        yaxis_title=y_axis_title,
        hovermode="x unified",
    )
    fig.update_xaxes(showgrid=False, tickfont=dict(color=MUTED))
    fig.update_yaxes(gridcolor=GRID, zeroline=False, tickfont=dict(color=MUTED))
    return fig


def render_line_chart(series: list[dict], title: str, y_axis_title: str, color_map: dict | None = None) -> None:
    frame = pd.DataFrame(series)
    fig = px.line(
        frame,
        x="quarter",
        y="value",
        color="series",
        markers=True,
        title=title,
        color_discrete_map=color_map,
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=7))
    _style_figure(fig, y_axis_title)
    st.plotly_chart(fig, use_container_width=True)


def render_bar_chart(items: list[dict], title: str, y_axis_title: str, color: str = "#2dd4bf") -> None:
    frame = pd.DataFrame(items)
    fig = px.bar(frame, x="label", y="value", title=title)
    fig.update_traces(marker_color=color, marker_line_color=color, marker_line_width=1)
    _style_figure(fig, y_axis_title)
    fig.update_xaxes(tickangle=0)
    st.plotly_chart(fig, use_container_width=True)


def render_gauge(score: int, title: str) -> None:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": title, "font": {"color": TEXT, "size": 16}},
            number={"font": {"color": "#f59e0b", "size": 34}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": MUTED},
                "bgcolor": PLOT_BG,
                "borderwidth": 0,
                "bar": {"color": "#f59e0b"},
                "steps": [
                    {"range": [0, 55], "color": "rgba(96,165,250,0.25)"},
                    {"range": [55, 75], "color": "rgba(45,212,191,0.25)"},
                    {"range": [75, 100], "color": "rgba(245,158,11,0.25)"}
                ],
            },
        )
    )
    fig.update_layout(paper_bgcolor=PLOT_BG, font_color=TEXT, margin=dict(l=10, r=10, t=60, b=10), height=240)
    st.plotly_chart(fig, use_container_width=True)
