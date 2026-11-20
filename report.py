"""Shared report markup for offline preview and the Streamlit app."""
from html import escape
from json import loads
from pathlib import Path

DATA_DIR = Path(__file__).with_name("data")
RESULTS = loads((DATA_DIR / "metrics.json").read_text(encoding="utf-8"))

CATEGORY_NAMES = {
    "Entertainment": "娱乐", "Music": "音乐", "Howto & Style": "教程与风格",
    "Comedy": "喜剧", "News & Politics": "新闻与政治", "People & Blogs": "人物与博客",
    "Sports": "体育", "Science & Technology": "科技", "Film & Animation": "影视与动画",
    "Education": "教育", "Pets & Animals": "宠物与动物", "Gaming": "游戏",
}
ITEM_NAMES = {
    "Cake": "蛋糕", "Tea": "茶", "Toast": "吐司", "Coffee": "咖啡",
    "Hot chocolate": "热巧克力", "Sandwich": "三明治", "Medialuna": "月牙面包",
    "Pastry": "酥皮点心",
}
UBER = "https://www.uber.com/us/en/blog/argos-real-time-alerts/"
SPOTIFY = "https://engineering.atspotify.com/2024/3/risk-aware-product-decisions-in-a-b-tests-with-multiple-metrics"
MICROSOFT = "https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/"

REPORT_CSS = """
.memo {
  --ink: #212121;
  --muted: #5e5e5e;
  --line: #dededb;
  color: var(--ink);
  font: 16px/1.7 -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
}
.memo * { box-sizing: border-box }
.memo h1,.memo h2,.memo h3 { color: var(--ink); line-height: 1.35; letter-spacing: normal }
.memo h1 { font-size: clamp(29px, 4vw, 36px); font-weight: 700; margin: 0 0 8px }
.memo h2 { font-size: 22px; font-weight: 650; margin: 0 0 8px }
.memo h3 { font-size: 16px; font-weight: 640; margin: 0 0 9px }
.memo p { margin: 0 0 10px }
.memo a { color: #303030; text-decoration: underline; text-underline-offset: 3px }
.memo a:focus-visible { outline: 2px solid #4b4b4b; outline-offset: 3px }
.memo .meta { font-size: 14px; color: var(--muted) }
.memo .meta-list { display: flex; flex-wrap: wrap; column-gap: 18px; padding: 0; margin: 0 0 16px; list-style: none }
.memo .meta-list li { margin: 0 }
.memo .decision { margin: 0 0 9px }
.memo .scope { color: var(--muted); font-size: 14px; font-variant-numeric: tabular-nums }
.memo .report-section { padding-top: 19px; margin-top: 22px; border-top: 1px solid var(--line) }
.memo .evidence { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 30px; margin: 17px 0 }
.memo figure { margin: 0; min-width: 0; padding: 0; break-inside: avoid }
.memo figcaption { font-size: 13px; color: var(--muted); margin-top: 8px; line-height: 1.55 }
.memo .bridge { display: flex; height: 10px; width: 100%; background: #ececea; margin: 13px 0 9px; overflow: hidden }
.memo .bridge .mix { background: #adadaa }
.memo .bridge .within { background: #4a4a48 }
.memo .legend { display: grid; gap: 3px; font-size: 14px; font-variant-numeric: tabular-nums }
.memo .legend > div { display: flex; justify-content: space-between; gap: 8px }
.memo .legend span { color: var(--muted) }
.memo .legend i { width: 8px; height: 8px; display: inline-block; margin-right: 6px; background: #adadaa }
.memo .legend .in i { background: #4a4a48 }
.memo .bars { margin-top: 9px; display: grid; gap: 6px }
.memo .bar { display: grid; grid-template-columns: 85px minmax(16px, 1fr) 56px; gap: 8px; align-items: center; font-size: 14px }
.memo .track { height: 6px; background: #ededeb; overflow: hidden }
.memo .track span { height: 100%; display: block; background: #5c5c5a }
.memo .bar b { text-align: right; font-variant-numeric: tabular-nums; font-weight: 600 }
.memo .table-scroll { overflow-x: auto }
.memo table { font-size: 14px; line-height: 1.45; width: 100%; border: 0; border-collapse: collapse; margin: 3px 0 0; font-variant-numeric: tabular-nums }
.memo th,.memo td { padding: 7px 8px; border: 0; border-bottom: 1px solid var(--line); vertical-align: top; text-align: right }
.memo td:first-child,.memo th:first-child { text-align: left; padding-left: 0 }
.memo td:last-child,.memo th:last-child { padding-right: 0 }
.memo th { border-top: 1px solid #9a9a96; border-bottom: 1px solid #9a9a96; color: #383838; font-weight: 650; white-space: nowrap }
.memo .narrative th,.memo .narrative td { text-align: left }
.memo .narrative td:first-child { min-width: 85px }
.memo figure .table-scroll table { font-size: 13px; margin-top: 5px }
.memo figure th,.memo figure td { padding-top: 5px; padding-bottom: 5px }
.memo .note { font-size: 14px; color: var(--muted); margin: 13px 0 7px }
.memo .note p { margin: 0 0 5px }
.memo .links { font-size: 14px; color: var(--muted); margin-top: 10px }
@media (max-width: 700px) {
  .memo .evidence { grid-template-columns: 1fr; gap: 17px }
  .memo .table-scroll table { min-width: 400px }
  .memo figure .table-scroll table { min-width: 310px }
  .memo .table-scroll .narrative { min-width: 0 }
}
@media print {
  .memo h2,.memo h3 { break-after: avoid }
  .memo thead { display: table-header-group }
  .memo tr { break-inside: avoid }
}
"""


def rate(value):
    return f"{100 * value:.2f}%"


def points(value):
    return f"{100 * value:+.2f}"


def table(headers, rows, narrative=False):
    attrs = ' class="narrative"' if narrative else ''
    headers = "".join(f'<th scope="col">{escape(item)}</th>' for item in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{escape(str(value))}</td>" for value in row) + "</tr>"
        for row in rows
    )
    return f'<div class="table-scroll" tabindex="0"><table{attrs}><thead><tr>{headers}</tr></thead><tbody>{body}</tbody></table></div>'


def scope(items):
    return '<p class="scope">' + "　·　".join(
        f"{escape(label)} {escape(str(value))}" for label, value in items
    ) + "</p>"


def bar_chart(items, scale, show_value):
    return '<div class="bars">' + "".join(
        f'<div class="bar"><span>{escape(label)}</span><div class="track" aria-hidden="true">'
        f'<span style="width:{min(100, max(0, value / scale * 100)):.2f}%"></span></div>'
        f'<b>{escape(show_value(value))}</b></div>'
        for label, value in items
    ) + "</div>"


def links(items):
    return '<p class="links">' + " · ".join(
        f'<a href="{escape(url, quote=True)}">{escape(label)}</a>' for label, url in items
    ) + "</p>"


def video_drivers():
    y = RESULTS["youtube"]
    drivers = []
    for item in y["categories"]:
        a, b = item["earlier_count"], item["later_count"]
        if min(a, b) >= 30:
            change = item["later_rate"] - item["earlier_rate"]
            contribution = b / y["later_count"] * change
            drivers.append(dict(
                category=CATEGORY_NAMES.get(item["category"], item["category"]),
                earlier_count=a, later_count=b, earlier_rate=item["earlier_rate"],
                later_rate=item["later_rate"], contribution=contribution,
            ))
    return sorted(drivers, key=lambda row: row["contribution"], reverse=True)


def basket_segments():
    return [
        dict(
            label=("周末" if row["day_type"] == "weekend" else "工作日") +
                  ("午前" if row["daypart"] == "before noon" else "12 点起"),
            orders=row["n"], joint=row["both"], rate=row["rate"],
        ) for row in RESULTS["basket"]["segments"]
    ]


def youtube_report():
    y = RESULTS["youtube"]
    drivers = video_drivers()
    total_change = y["later_rate"] - y["earlier_rate"]
    within_share = y["within_delta"] / total_change
    top_three = sum(row["contribution"] for row in drivers[:3])
    lead, second, third = drivers[:3]
    class_rows = [
        (row["category"], row["earlier_count"], row["later_count"],
         rate(row["earlier_rate"]), rate(row["later_rate"]), points(row["contribution"]))
        for row in drivers[:6]
    ]
    driver_rows = table(
        ["类目", "前段样本", "后段样本", "前段复上榜率", "后段复上榜率", "类目内贡献（百分点）"],
        class_rows,
    )
    bridge = f"""
      <div class="bridge" aria-label="类目结构项 {points(y['mix_delta'])} 个百分点。类目内项 {points(y['within_delta'])} 个百分点">
        <div class="mix" style="width:{(1-within_share)*100:.3f}%"></div>
        <div class="within" style="width:{within_share*100:.3f}%"></div>
      </div>
      <div class="legend">
        <div><span><i></i>类目结构变化</span><b>{points(y['mix_delta'])} 个百分点</b></div>
        <div class="in"><span><i></i>类目内表现变化</span><b>{points(y['within_delta'])} 个百分点</b></div>
      </div>"""
    return f"""
<article class="memo" id="youtube">
  <header class="page-head">
    <h1>YouTube 热榜复盘</h1>
    <ul class="meta meta-list"><li>YouTube 美国区历史热榜</li><li>{y['chart_start']} 至 {y['chart_end']}</li><li>分组日期 {y['period_split']}</li></ul>
    <p class="decision"><b>结论</b>　复上榜率从 <b>{rate(y['earlier_rate'])}</b> 升至 <b>{rate(y['later_rate'])}</b>。
      约 <b>{within_share:.0%}</b> 的增幅来自类目内部变化。先回查{lead['category']}、{second['category']}和{third['category']}的频道与发布时间分布，等证据齐备后再决定是否调整类目配比。</p>
    {scope([("原始日榜记录",y["raw_rows"]),("去重后视频日",y["unique_video_days"]),("纳入分析的视频",y["eligible_videos"]),("整体变化",points(total_change)+" 个百分点")])}
  </header>
  <section class="report-section">
    <h2>类目内部贡献 {points(y['within_delta'])} 个百分点</h2>
    <p>如果类目表现停留在前段、只换成后段的类目占比，整体只会到 <b>{rate(y['weighted_later_rate'])}</b>。剩下的差值才归入类目内部变化。</p>
    <div class="evidence">
      <figure><h3>整体变化拆解</h3>{bridge}
        <figcaption>前段实际 {rate(y['earlier_rate'])} → 只改变类目权重 {rate(y['weighted_later_rate'])} → 后段实际 {rate(y['later_rate'])}。分项按各自精度四舍五入。</figcaption></figure>
      <figure><h3>类目内贡献前五</h3>
        {bar_chart([(row['category'],row['contribution']) for row in drivers[:5]], .017, points)}
        <figcaption>单位为百分点。类目贡献 = 后段样本占比 × 类目复上榜率变化。</figcaption></figure>
    </div>
    <p>{lead['category']}是首要排查对象，类目内增幅约 {points(lead['later_rate']-lead['earlier_rate'])} 个百分点，但后段样本占比较高。
      {second['category']}自身提升更大。前三类合计贡献 <b>{points(top_three)} 个百分点</b>，占类目内项 {top_three/y['within_delta']:.0%}。</p>
    {driver_rows}
  </section>
  <section class="report-section">
    <h2>排查顺序与证据要求</h2>
    {table(["先查什么","看哪些数据","怎样解释"],[
       ("采集口径","日榜采集日志、每日覆盖条数、类目映射版本","先排除采集覆盖或映射变化造成的观测偏差。"),
       ("头部频道与发布节奏","频道 ID、首次上榜前的视频年龄、周内分布","按频道和发布时间分层；比较剔除头部频道后的差值。"),
       ("分发机制","推荐曝光、榜单规则变更记录、端和地区","若与明确变更重合，再用随机对照或可比流量验证机制。")
    ],narrative=True)}
    <div class="note"><p><b>指标口径</b>　视频在样本中首见起 7 个自然日内至少 3 天在榜，首见当天计入。
      排除样本首日及观察窗缺报的记录，前段 {y['earlier_count']} 个、后段 {y['later_count']} 个视频。任一时段样本不足 30 个的类目合并为「其他」。</p>
      <p><b>分析边界</b>　样本来自榜单，能比较上榜视频的持续表现。曝光、受众和策略效果需要平台侧数据验证。</p></div>
    {links([("公开日榜数据","https://www.kaggle.com/datasets/datasnaek/youtube-new"),("Kaggle 项目参考","https://www.kaggle.com/code/ammar111/youtube-trending-videos-analysis"),("排查思路参考 · Uber Argos",UBER)])}
  </section>
</article>"""


def basket_report():
    b = RESULTS["basket"]
    pair = b["selected_pair"]
    tea_rate = pair["holdout_confidence"] / pair["holdout_lift"]
    segment_rows = basket_segments()
    wanted = [("Cake","Tea"),("Toast","Coffee"),("Hot chocolate","Cake"),("Medialuna","Pastry")]
    rules = {(row["anchor"],row["add_on"]):row for row in b["top_rules"]}
    comparisons = []
    for key in wanted:
        row = rules[key]
        name = f"{ITEM_NAMES[row['anchor']]} → {ITEM_NAMES[row['add_on']]}"
        comparisons.append((name,row["discovery_orders"],row["holdout_anchor_orders"],
                            row["holdout_joint_orders"],rate(row["holdout_confidence"]),
                            f"{row['holdout_lift']:.2f}"))
    return f"""
<article class="memo" id="basket">
  <header class="page-head">
    <h1>购物车联购评审</h1>
    <ul class="meta meta-list"><li>Bread Basket 线下门店订单</li><li>{b['from_date']} 至 {b['to_date']}</li><li>留出组起点 {b['cutoff']}</li><li>实验待运行</li></ul>
    <p class="decision"><b>结论</b>　先测试<b>加购蛋糕时推荐茶</b>。留出组 {pair['holdout_anchor_orders']} 笔蛋糕单中有
      {pair['holdout_joint_orders']} 笔同时买茶，联购率 <b>{rate(pair['holdout_confidence'])}</b>，约为全体订单买茶率的
      <b>{pair['holdout_lift']:.2f} 倍</b>。另一个高 Lift 组合「热巧克力 → 蛋糕」只有 130 笔触发商品订单，适合作为后续备选。</p>
    {scope([("有效订单",b["total_orders"]),("留出订单",b["holdout_orders"]),("后期 Lift > 1 的规则",f'{b["holdout_stable_rules"]}/{b["qualified_rules"]} 条'),("建议实验样本量",f'{b["sample_per_arm"]} 人/组')])}
  </header>
  <section class="report-section">
    <h2>早期找组合，后期检查规模与稳定性</h2>
    <p>从 {b['raw_lines']} 条流水还原 {b['total_orders']} 笔订单。早期组 {b['discovery_orders']} 单，按共购量、置信度和 Lift 初筛，
      再用后期 {b['holdout_orders']} 单回测。表中保留一个后期 Lift 低于 1 的组合，便于看到筛选带来的变化。</p>
    {table(["搭售方向","早期共购单","后期含触发商品单","后期共购单","后期联购率","后期 Lift"], comparisons)}
    <div class="evidence">
      <figure><h3>茶购买率基准</h3>
        {bar_chart([("全体订单",tea_rate),("含蛋糕订单",pair['holdout_confidence'])],.30,rate)}
        <figcaption>同一后期样本。含蛋糕订单联购率的 Wilson 95% 区间为 {rate(pair['holdout_ci_low'])} 至 {rate(pair['holdout_ci_high'])}。</figcaption></figure>
      <figure><h3>蛋糕与茶的时段分布</h3>
        {table(["时段","含蛋糕单","共购单","联购率"],[(r["label"],r["orders"],r["joint"],rate(r["rate"])) for r in segment_rows])}
        <figcaption>周末午前分母只有 49 单，暂不据此设置单独的时段策略。</figcaption></figure>
    </div>
  </section>
  <section class="report-section">
    <h2>实验设计与上线决策</h2>
    {table(["环节","设计"],[
       ("资格与分流","用户首次加购蛋糕、茶可售且购物车中没有茶时进入实验。按用户 ID 固定 1:1 随机分流。"),
       ("对照组与实验组","对照组沿用原推荐位；实验组在同一位置展示茶。两组记录资格、分流、曝光与支付事件。"),
       ("主指标","从触发起 24 小时内购买茶的用户数 ÷ 所有纳入分流的用户数。按随机分组分析。"),
       ("护栏与质量","护栏为支付转化率、每位分流用户毛利及退款率。启动前写明可接受的下降幅度；先查样本比例失衡和埋点完备性。"),
       ("上线与复盘","分流质量过关，主指标置信区间支持正向增量、各项护栏通过时，考虑逐步放量。证据不足则保留现状并复盘。"),
    ],narrative=True)}
    <div class="note"><p><b>样本估算</b>　以历史完单联购率 {rate(pair['holdout_confidence'])} 作演示基线，最小可检测差异 3 个百分点，双侧 α=0.05、功效 80%，约需每组 {b['sample_per_arm']} 人。排期应覆盖完整周周期。</p>
      <p><b>证据边界</b>　门店历史数据提供候选排序，缺少未成交购物车、曝光和毛利记录。上线前用触发人群实际购买率重算样本，同时按护栏所需样本量取更大的值。</p></div>
    {links([("Kaggle 项目参考","https://www.kaggle.com/code/xvivancos/market-basket-analysis"),("订单数据公开镜像","https://github.com/luis-alarcon/Kaggle_BreadBasket/blob/master/dataset/BreadBasket_DMS.csv"),("上线决策参考 · Spotify",SPOTIFY),("分流检查参考 · Microsoft",MICROSOFT)])}
  </section>
</article>"""
