"""Streamlit-specific controls beneath the shared business reports."""
from math import ceil, sqrt
from statistics import NormalDist

import pandas as pd
import streamlit as st

from report import (
    CATEGORY_NAMES, DATA_DIR, REPORT_CSS, RESULTS, basket_report, youtube_report,
)


def show_report(article):
    st.html(f"<style>{REPORT_CSS}</style>{article}")


def youtube():
    y = RESULTS["youtube"]
    show_report(youtube_report())
    with st.expander("按样本量筛选类目明细"):
        min_count = st.slider("每段最少视频数", 10, 200, 30, 10)
        rows = []
        for item in y["categories"]:
            a, b = item["earlier_count"], item["later_count"]
            if min(a, b) < min_count:
                continue
            rows.append({
                "类目": CATEGORY_NAMES.get(item["category"], item["category"]),
                "前段样本": a,
                "后段样本": b,
                "前段复上榜率": item["earlier_rate"] * 100,
                "后段复上榜率": item["later_rate"] * 100,
                "类目内贡献": b / y["later_count"] * (item["later_rate"] - item["earlier_rate"]) * 100,
            })
        rows.sort(key=lambda row: row["类目内贡献"], reverse=True)
        st.dataframe(
            pd.DataFrame(rows),
            hide_index=True, width="stretch",
            column_config={
                "前段样本": st.column_config.NumberColumn(format="%d"),
                "后段样本": st.column_config.NumberColumn(format="%d"),
                "前段复上榜率": st.column_config.NumberColumn(format="%.2f%%"),
                "后段复上榜率": st.column_config.NumberColumn(format="%.2f%%"),
                "类目内贡献": st.column_config.NumberColumn("类目内贡献（百分点）", format="%+.2f"),
            },
        )
        st.caption("筛选器控制明细展示。报告中的结构和类目内贡献按固定分组口径计算。")
        st.download_button(
            "下载类目明细 CSV", (DATA_DIR / "youtube_category_metrics.csv").read_bytes(),
            file_name="youtube_category_metrics.csv", mime="text/csv",
        )


def sample_size(baseline, delta):
    target = baseline + delta
    if target >= 1:
        raise ValueError("基线加最小可检测差异必须低于 100%。")
    pooled = (baseline + target) / 2
    normal = NormalDist()
    numerator = (
        normal.inv_cdf(.975) * sqrt(2 * pooled * (1 - pooled))
        + normal.inv_cdf(.8) * sqrt(baseline * (1 - baseline) + target * (1 - target))
    )
    return ceil((numerator / delta) ** 2)


def basket():
    b = RESULTS["basket"]
    show_report(basket_report())
    with st.expander("按实际基线重算实验人数"):
        left, right = st.columns(2)
        baseline = left.number_input(
            "触发用户基线（%）", 1.0, 90.0, b["selected_pair"]["holdout_confidence"] * 100,
            1.0, format="%.4f",
        )
        delta = right.number_input(
            "最小可检测差异（百分点）", 0.5, 8.0, b["experiment_mde"] * 100,
            0.5, format="%.1f",
        )
        needed = sample_size(baseline / 100, delta / 100)
        st.markdown(f"主指标每组约 **{needed} 人**。双侧 α = 0.05，功效 80%。")
        st.caption("默认值用于演示，正式排期还需纳入护栏指标所需样本。")
        st.download_button(
            "下载候选搭售规则 CSV", (DATA_DIR / "basket_rules.csv").read_bytes(),
            file_name="basket_rules.csv", mime="text/csv",
        )
