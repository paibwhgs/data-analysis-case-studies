# 内容与零售分析案例

供 Streamlit Community Cloud 部署。只包含公开样本的汇总结果，不含简历、个人联系方式、实习资料或原始用户数据。

## 本地运行

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

主页展示 YouTube 热榜分析，`/basket` 展示购物篮联购。主页支持按类目样本量筛选，联购页支持调整实验基线和最小可检测差异。两页均可下载汇总 CSV。

## Community Cloud

将本目录中的 `app.py`、`requirements.txt`、`case_studies.py`、`report.py`、`views/`、`.streamlit/`、`data/` 放到同一个 GitHub 仓库，在 [Streamlit Community Cloud](https://share.streamlit.io/) 选择该仓库、分支和 `app.py`。发布后以控制台返回的 `.streamlit.app` 地址为准，联购页路径追加 `/basket`。

[Streamlit 官方部署说明](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)

网页正文的结构参考 Uber Argos 的异常排查、Spotify 的实验上线决策和 Microsoft 的分流质量检查。来源与数据口径见各案例底部。
