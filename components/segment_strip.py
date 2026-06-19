import streamlit as st


SEGMENT_CLASSES = ["teal", "blue", "amber", "purple", "red"]


def render_segment_strip(segments: list[dict]) -> None:
    cols = st.columns(len(segments))
    for idx, (col, seg) in enumerate(zip(cols, segments)):
        with col:
            tone = SEGMENT_CLASSES[idx % len(SEGMENT_CLASSES)]
            st.markdown(
                f"""
                <div class='mesh-card-compact mesh-segment-card'>
                  <div class='mesh-kpi-label'>{seg['label']}</div>
                  <div class='mesh-kpi-value mesh-segment-median'>{seg['median']}</div>
                  <div class='mesh-segment-heat-row'>
                    <div class='mesh-segment-heat-track'>
                      <div class='mesh-segment-heat-fill mesh-segment-heat-{tone}' style='width:{seg['heat']}%'></div>
                    </div>
                    <span>{seg['heat']}</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
