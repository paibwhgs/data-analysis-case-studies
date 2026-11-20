import streamlit as st

st.set_page_config(page_title="内容与零售分析案例", layout="wide")
st.html("""<style>
[data-testid="stMainBlockContainer"]{max-width:980px;padding-top:2rem}
</style>""")
st.navigation(
    [
        st.Page("views/youtube.py", title="YouTube 热榜复盘", default=True),
        st.Page("views/basket.py", title="购物车联购评审", url_path="basket"),
    ],
    position="top",
).run()
