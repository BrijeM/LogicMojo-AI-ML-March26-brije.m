from __future__ import annotations

import html
import math
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd


ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "dataset"
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"


REPORT_CONTENT = {
    "Project Title": [
        "Brije Ecommerce Intelligence Project: Customer, Revenue, Product, Seller, and Satisfaction Analytics"
    ],
    "Business Problem Statement": [
        "The business needs a clear view of marketplace performance across customers, orders, products, sellers, payments, delivery, and reviews. The goal of this project is to combine raw e-commerce datasets into an analytical view that helps identify revenue drivers, customer behavior patterns, operational bottlenecks, and satisfaction risks. These insights can support decisions around category focus, seller management, customer retention, payment strategy, and delivery improvement."
    ],
    "Dataset Description": [
        "The project uses multiple relational e-commerce datasets stored in the dataset/ folder:",
        [
            "orders.csv: 99,441 orders with order status and purchase, approval, shipping, delivery, and estimated delivery timestamps.",
            "order_item.csv: 112,650 order-item records with product, seller, price, freight value, and shipping limit details.",
            "payments.csv: 103,886 payment records with payment type, installments, and payment value.",
            "reviews.csv: 104,719 review records with review score, comments, and review timestamps.",
            "products.csv: 32,951 product records with category, description, photo, weight, and size attributes.",
            "customers.csv: 99,441 customer records with unique customer IDs and customer location details.",
            "sellers.csv: 3,095 seller records with seller city and state.",
            "location.csv: 1,000,163 geolocation records by zip-code prefix.",
            "category_translation.csv: 70 category translation records mapping original category names to English labels.",
        ],
        "The data covers orders purchased from September 4, 2016 through October 17, 2018.",
    ],
    "Methodology": [
        [
            "Loaded and inspected all source datasets to understand record counts, columns, data types, missing values, duplicates, and key relationships.",
            "Cleaned and prepared the data by converting timestamp columns to datetime format, validating numeric fields, removing duplicate records where needed, and standardizing analysis-ready fields.",
            "Integrated the datasets using common keys such as order_id, customer_id, product_id, seller_id, and product_category_name.",
            "Engineered business features including total order value, item count, delivery days, late delivery flag, purchase month, customer repeat status, customer value, category revenue, seller revenue, and dissatisfaction indicators.",
            "Performed exploratory data analysis across customer behavior, revenue trends, product categories, seller contribution, payment preferences, delivery performance, and review scores.",
            "Summarized findings into business recommendations focused on growth, retention, logistics, and customer satisfaction.",
        ]
    ],
    "Key Findings": [
        [
            "The marketplace processed 99,441 total orders, of which 96,478 were delivered.",
            "Total item-plus-freight revenue was 15,843,553.24, with an average order value of 159.33.",
            "Repeat customer share was only 3.1%, indicating a large opportunity to improve retention and loyalty.",
            "Average review score was 4.09, showing generally positive customer satisfaction, but dissatisfaction is highly connected to delivery performance.",
            "Average delivery time was 12.6 days, and 7.9% of orders were delivered after the estimated delivery date.",
            "Late delivery is a major satisfaction risk: dissatisfied reviews, defined as review scores of 1 or 2, occurred in 52.9% of late deliveries compared with 11.3% of on-time or early deliveries.",
            "The highest revenue categories were health and beauty, watches and gifts, bed bath table, sports leisure, and computers accessories.",
            "The highest item-volume categories were bed bath table, health and beauty, sports leisure, furniture decor, and computers accessories.",
            "Customer demand was geographically concentrated, with the largest unique-customer states being SP, RJ, MG, RS, and PR.",
            "Credit card was the dominant payment method at 73.9% of payment records, followed by boleto at 19.0%.",
            "Revenue was distributed across many sellers: the top 10 sellers contributed 12.8% of total seller revenue, suggesting the marketplace is not overly dependent on a small seller group.",
        ]
    ],
    "Business Insights": [
        [
            "Delivery reliability is one of the strongest controllable drivers of customer satisfaction. Late orders show a much higher low-rating rate than on-time or early orders.",
            "The platform has strong acquisition but weak repeat behavior. Most customers purchase once, so retention programs can create meaningful incremental revenue.",
            "Revenue and demand are concentrated in a few leading product categories, making category-level merchandising and inventory planning important for growth.",
            "Demand is geographically concentrated in major states, especially SP, RJ, and MG, which can guide regional logistics planning and marketing allocation.",
            "Seller revenue is broad-based rather than dominated by only a few sellers, so marketplace health depends on improving the performance of a wide seller base.",
            "Credit card usage dominates payments, but boleto remains large enough to keep as a priority payment option for customer accessibility.",
        ]
    ],
    "Recommendations": [
        [
            "Prioritize delivery reliability by monitoring late-delivery rates, carrier performance, and seller shipping-limit compliance.",
            "Create retention campaigns for first-time customers, especially in high-demand states and top product categories.",
            "Invest in inventory, merchandising, and promotions for high-performing categories such as health and beauty, watches and gifts, and bed bath table.",
            "Build seller scorecards that combine revenue, fulfillment speed, late delivery, review score, and cancellation behavior.",
            "Improve customer communication for orders at risk of delay to reduce dissatisfaction and protect review scores.",
            "Maintain credit-card optimization while continuing to support boleto customers, since both represent meaningful payment behavior.",
        ]
    ],
    "Visual Outputs": [
        "The following labeled and readable chart files are included in reports/figures/:",
        [
            "monthly_revenue_trend.svg",
            "top_categories_by_revenue.svg",
            "review_score_distribution.svg",
            "delivery_dissatisfaction_rate.svg",
            "top_customer_states.svg",
            "payment_method_distribution.svg",
            "seller_revenue_concentration.svg",
        ],
    ],
}


def money_short(value: float) -> str:
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:.0f}K"
    return f"{value:.0f}"


def slug_label(value: str) -> str:
    return value.replace("_", " ").title()


def svg_text(x, y, text, size=14, fill="#1f2937", anchor="start", weight="400"):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
        f'font-weight="{weight}">{html.escape(str(text))}</text>'
    )


def horizontal_bar_chart(path, title, labels, values, x_label, color="#2f6f9f", formatter=money_short):
    width, height = 1100, 680
    left, right, top, bottom = 260, 70, 90, 95
    chart_w = width - left - right
    chart_h = height - top - bottom
    max_v = max(values) * 1.18
    step = chart_h / len(labels)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(width / 2, 42, title, 26, "#111827", "middle", "700"),
        svg_text(left + chart_w / 2, height - 28, x_label, 15, "#374151", "middle", "600"),
    ]
    for i in range(6):
        x = left + chart_w * i / 5
        value = max_v * i / 5
        lines.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top + chart_h}" stroke="#e5e7eb" stroke-width="1"/>')
        lines.append(svg_text(x, top + chart_h + 25, formatter(value), 12, "#6b7280", "middle"))
    for idx, (label, value) in enumerate(zip(labels, values)):
        y = top + idx * step + step * 0.18
        bar_h = step * 0.62
        bar_w = chart_w * value / max_v
        lines.append(svg_text(left - 14, y + bar_h * 0.66, label, 14, "#374151", "end", "600"))
        lines.append(f'<rect x="{left}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="3" fill="{color}"/>')
        lines.append(svg_text(left + bar_w + 8, y + bar_h * 0.66, formatter(value), 13, "#111827", "start", "700"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def vertical_bar_chart(path, title, labels, values, y_label, color="#2a9d8f", formatter=lambda v: f"{v:,.0f}"):
    width, height = 1000, 620
    left, right, top, bottom = 95, 50, 90, 105
    chart_w = width - left - right
    chart_h = height - top - bottom
    max_v = max(values) * 1.20
    bar_gap = 28
    bar_w = (chart_w - bar_gap * (len(values) - 1)) / len(values)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(width / 2, 42, title, 26, "#111827", "middle", "700"),
        svg_text(24, top + chart_h / 2, y_label, 15, "#374151", "middle", "600") + f'<animateTransform attributeName="transform" type="rotate" from="-90 24 {top + chart_h / 2}" to="-90 24 {top + chart_h / 2}" dur="0.01s" fill="freeze"/>',
    ]
    for i in range(6):
        y = top + chart_h - chart_h * i / 5
        value = max_v * i / 5
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_w}" y2="{y:.1f}" stroke="#e5e7eb" stroke-width="1"/>')
        lines.append(svg_text(left - 12, y + 4, formatter(value), 12, "#6b7280", "end"))
    for idx, (label, value) in enumerate(zip(labels, values)):
        x = left + idx * (bar_w + bar_gap)
        bar_h = chart_h * value / max_v
        y = top + chart_h - bar_h
        lines.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="3" fill="{color}"/>')
        lines.append(svg_text(x + bar_w / 2, y - 8, formatter(value), 12, "#111827", "middle", "700"))
        lines.append(svg_text(x + bar_w / 2, top + chart_h + 30, label, 14, "#374151", "middle", "600"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def line_chart(path, title, labels, values, y_label, color="#2563eb", formatter=money_short):
    width, height = 1200, 650
    left, right, top, bottom = 95, 50, 90, 130
    chart_w = width - left - right
    chart_h = height - top - bottom
    min_v, max_v = min(values), max(values)
    low = 0 if min_v > 0 else min_v
    high = max_v * 1.15
    points = []
    for idx, value in enumerate(values):
        x = left + chart_w * idx / (len(values) - 1)
        y = top + chart_h - chart_h * (value - low) / (high - low)
        points.append((x, y))
    path_data = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(width / 2, 42, title, 26, "#111827", "middle", "700"),
        svg_text(25, top + chart_h / 2, y_label, 15, "#374151", "middle", "600") + f'<animateTransform attributeName="transform" type="rotate" from="-90 25 {top + chart_h / 2}" to="-90 25 {top + chart_h / 2}" dur="0.01s" fill="freeze"/>',
    ]
    for i in range(6):
        y = top + chart_h - chart_h * i / 5
        value = low + (high - low) * i / 5
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_w}" y2="{y:.1f}" stroke="#e5e7eb" stroke-width="1"/>')
        lines.append(svg_text(left - 12, y + 4, formatter(value), 12, "#6b7280", "end"))
    lines.append(f'<polyline points="{path_data}" fill="none" stroke="{color}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>')
    for x, y in points:
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')
    tick_every = max(1, math.ceil(len(labels) / 10))
    for idx, label in enumerate(labels):
        if idx % tick_every == 0 or idx == len(labels) - 1:
            x = left + chart_w * idx / (len(values) - 1)
            lines.append(svg_text(x, top + chart_h + 30, label, 12, "#374151", "middle", "600"))
    peak_idx = max(range(len(values)), key=lambda i: values[i])
    peak_x, peak_y = points[peak_idx]
    lines.append(svg_text(peak_x, peak_y - 16, f"Peak {labels[peak_idx]}: {formatter(values[peak_idx])}", 13, "#b91c1c", "middle", "700"))
    lines.append("</svg>")
    path.write_text("\n".join(lines), encoding="utf-8")


def wrap_lines(text, max_chars=80):
    words = text.split()
    lines, current = [], []
    for word in words:
        if sum(len(w) for w in current) + len(current) + len(word) > max_chars:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines


def make_markdown():
    lines = ["# Brije Ecommerce Intelligence Project Report", ""]
    for section, blocks in REPORT_CONTENT.items():
        lines += [f"## {section}", ""]
        for block in blocks:
            if isinstance(block, list):
                for item in block:
                    lines.append(f"- {item}")
                lines.append("")
            else:
                lines += [block, ""]
    (REPORTS / "project_report.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def docx_paragraph(text="", style=None, bold=False):
    p_style = ""
    if style:
        p_style = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
    b = "<w:b/>" if bold else ""
    return (
        f"<w:p>{p_style}<w:r><w:rPr>{b}</w:rPr><w:t xml:space=\"preserve\">"
        f"{escape(text)}"
        "</w:t></w:r></w:p>"
    )


def make_docx():
    body = [docx_paragraph("Brije Ecommerce Intelligence Project Report", "Title")]
    for section, blocks in REPORT_CONTENT.items():
        body.append(docx_paragraph(section, "Heading1"))
        for block in blocks:
            if isinstance(block, list):
                for item in block:
                    body.append(docx_paragraph(f"• {item}", "ListParagraph"))
            else:
                for line in wrap_lines(block, 120):
                    body.append(docx_paragraph(line))
    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {''.join(body)}
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="720"/></w:sectPr>
  </w:body>
</w:document>'''
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>'''
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''
    doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr><w:pPr><w:spacing w:after="280"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="280" w:after="120"/></w:pPr><w:rPr><w:b/><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/><w:pPr><w:ind w:left="360" w:hanging="180"/><w:spacing w:after="80"/></w:pPr></w:style>
</w:styles>'''
    with zipfile.ZipFile(REPORTS / "project_report.docx", "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/_rels/document.xml.rels", doc_rels)
        docx.writestr("word/document.xml", document)
        docx.writestr("word/styles.xml", styles)


def build_data():
    orders = pd.read_csv(DATASET / "orders.csv", parse_dates=["order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"])
    items = pd.read_csv(DATASET / "order_item.csv")
    payments = pd.read_csv(DATASET / "payments.csv")
    reviews = pd.read_csv(DATASET / "reviews.csv")
    products = pd.read_csv(DATASET / "products.csv")
    customers = pd.read_csv(DATASET / "customers.csv")
    sellers = pd.read_csv(DATASET / "sellers.csv")
    translation = pd.read_csv(DATASET / "category_translation.csv")
    items["item_total"] = items["price"] + items["freight_value"]
    return orders, items, payments, reviews, products, customers, sellers, translation


def make_figures():
    orders, items, payments, reviews, products, customers, sellers, translation = build_data()
    order_values = items.groupby("order_id", as_index=False).agg(total_order_value=("item_total", "sum"))
    monthly = orders.merge(order_values, on="order_id", how="left").dropna(subset=["order_purchase_timestamp"])
    monthly["month"] = monthly["order_purchase_timestamp"].dt.to_period("M").dt.to_timestamp()
    monthly_summary = monthly.groupby("month", as_index=False).agg(revenue=("total_order_value", "sum")).sort_values("month")
    line_chart(
        FIGURES / "monthly_revenue_trend.svg",
        "Monthly Revenue Trend",
        monthly_summary["month"].dt.strftime("%b %Y").tolist(),
        monthly_summary["revenue"].fillna(0).tolist(),
        "Revenue",
    )

    category = items.merge(products[["product_id", "product_category_name"]], on="product_id", how="left").merge(translation, on="product_category_name", how="left")
    category_summary = category.groupby("product_category_name_english", as_index=False).agg(revenue=("item_total", "sum")).sort_values("revenue", ascending=False).head(10)
    category_summary = category_summary.sort_values("revenue")
    horizontal_bar_chart(
        FIGURES / "top_categories_by_revenue.svg",
        "Top 10 Product Categories by Revenue",
        [slug_label(v) for v in category_summary["product_category_name_english"]],
        category_summary["revenue"].tolist(),
        "Revenue",
        "#2f6f9f",
    )

    review_counts = reviews["review_score"].value_counts().reindex([1, 2, 3, 4, 5]).fillna(0)
    vertical_bar_chart(
        FIGURES / "review_score_distribution.svg",
        "Review Score Distribution",
        [str(v) for v in review_counts.index],
        review_counts.tolist(),
        "Orders",
        "#2a9d8f",
    )

    delivery = orders.merge(reviews[["order_id", "review_score"]], on="order_id", how="left")
    delivery["late_delivery"] = delivery["order_delivered_customer_date"] > delivery["order_estimated_delivery_date"]
    delivery["is_dissatisfied"] = delivery["review_score"] <= 2
    rates = delivery.groupby("late_delivery")["is_dissatisfied"].mean().reindex([False, True]).fillna(0) * 100
    vertical_bar_chart(
        FIGURES / "delivery_dissatisfaction_rate.svg",
        "Dissatisfaction Rate by Delivery Status",
        ["On Time / Early", "Late"],
        rates.tolist(),
        "Dissatisfied Orders (%)",
        "#d1495b",
        lambda v: f"{v:.1f}%",
    )

    state_counts = customers.drop_duplicates("customer_unique_id")["customer_state"].value_counts().head(10).sort_values()
    horizontal_bar_chart(
        FIGURES / "top_customer_states.svg",
        "Top 10 Customer States",
        state_counts.index.tolist(),
        state_counts.tolist(),
        "Unique Customers",
        "#4c78a8",
        lambda v: f"{v:,.0f}",
    )

    payment_share = payments["payment_type"].value_counts(normalize=True).mul(100).sort_values().tail(5)
    horizontal_bar_chart(
        FIGURES / "payment_method_distribution.svg",
        "Payment Method Distribution",
        [slug_label(v) for v in payment_share.index],
        payment_share.tolist(),
        "Payment Records (%)",
        "#f58518",
        lambda v: f"{v:.1f}%",
    )

    seller_summary = items.groupby("seller_id", as_index=False).agg(revenue=("item_total", "sum")).sort_values("revenue", ascending=False)
    seller_summary["cumulative_revenue_share"] = seller_summary["revenue"].cumsum() / seller_summary["revenue"].sum() * 100
    seller_summary["rank"] = range(1, len(seller_summary) + 1)
    sample = pd.concat([seller_summary.head(50), seller_summary.iloc[49::100]]).drop_duplicates("seller_id").sort_values("rank")
    line_chart(
        FIGURES / "seller_revenue_concentration.svg",
        "Cumulative Seller Revenue Contribution",
        [str(v) for v in sample["rank"]],
        sample["cumulative_revenue_share"].tolist(),
        "Cumulative Revenue Share (%)",
        "#7b6fd6",
        lambda v: f"{v:.0f}%",
    )


def main():
    REPORTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    make_markdown()
    make_docx()
    make_figures()


if __name__ == "__main__":
    main()
