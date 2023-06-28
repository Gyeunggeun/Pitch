import streamlit as st
def custom_metric_card(label, value, delta, label_color, text_color, delta_color):
    delta_symbol = ""
    if delta == "증가":
        delta_symbol = "↑"
    elif delta == "감소":
        delta_symbol = "↓"
    card_html = f"""
    <div style="position: relative; display: inline-block; padding: 0rem 1rem; 
                margin: 0.25rem; width: 16vw; height: 12.3vh; background: #CBD8EC; 
                border-left: 10px solid #82A9E8; border-radius: 0.5rem; box-shadow: 0 0.25rem 1.75rem 0 rgba(58, 59, 69, 0.15);">
        <h4 style="position: absolute; top: -10%; left: 0%; color: {label_color}; font-size: 1vw; font-weight: normal; font-family: 'Arial';">{label}</h4>
        <h2 style="position: absolute; bottom: 0%; left: 10%; color: {text_color}; font-size: 2.2vw; font-family: 'Avenir Next';">{value}</h2>
        <h4 style="position: absolute; bottom: -30%; left: 40%; color: {delta_color}; font-size: 1vw; font-weight: normal;">{delta_symbol} {delta}</h4>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)



def style_metric_cards(
    background_color: str = "#CBD8EC", # 배경 색상 변경
    border_size_px: int = 1,
    border_color: str = "#CCC",
    border_radius_px: int = 5,
    border_left_color: str = "#82A9E8",
    box_shadow: bool = True,
    text_colors: list = ["#840A54", "#840A54", "#840A54"],   # 텍스트 색상 변경
    label_colors: list = ["#606770", "#606770", "#606770"],  # 라벨 색상을 변경
    arrow_color: str = "#00FF00",  # 화살표 옆 숫자 색상을 변경
):
    for i in range(3):
        box_shadow_str = (
            "box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;"
            if box_shadow
            else "box-shadow: none !important;"
        )
        st.markdown(
            f"""
            <style>
                div[data-testid="metric-container"]:nth-child({i+1}) {{
                    background-color: {background_color};
                    border: {border_size_px}px solid {border_color};
                    padding: 3% 5% 3% 10%;
                    border-radius: {border_radius_px}px;
                    border-left: 0.5rem solid {border_left_color} !important;
                    color: {text_colors[i]} !important;
                    line-height: 0.9;
                    font-size: 0.8rem;
                }}
                div[data-testid="stMarkdownContainer"].css-1xzm5la.eqr7zpz4:nth-child({i+1}) {{
                    color: {label_colors[i]} !important;
                }}
                div[data-testid="stMarkdownContainer"].css-wnm74r.e1vioofd0 {{
                    color: {arrow_color} !important;
                }}
                {box_shadow_str}
            </style>
            """,
            unsafe_allow_html=True,
        )