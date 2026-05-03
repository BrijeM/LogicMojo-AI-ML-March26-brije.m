# Brije Ecommerce Intelligence Project

This repository contains an end-to-end e-commerce analytics project using customer, order, payment, product, seller, location, and review datasets.

## Project Objective

The goal of this project is to create a unified business view of marketplace performance and identify insights related to revenue, customers, product categories, sellers, payment behavior, delivery performance, and customer satisfaction.

## Deliverables

- `ecommerce_project.ipynb`: notebook with data loading, cleaning, integration, feature engineering, EDA, and recommendations
- `reports/project_report.docx`: final project report in Word format
- `reports/project_report.md`: Markdown copy of the project report
- `reports/visual_outputs.html`: visual-output gallery for reviewing all charts together
- `reports/figures/`: exported visual charts and graphs
- `build_report_artifacts.py`: script used to regenerate the report files and chart outputs

## Report Sections

The project report includes:

- Project Title
- Business Problem Statement
- Dataset Description
- Methodology
- Key Findings
- Business Insights
- Recommendations
- Visual Outputs

## Visual Outputs

The following charts are available in `reports/figures/`:

- `monthly_revenue_trend.svg`
- `top_categories_by_revenue.svg`
- `review_score_distribution.svg`
- `delivery_dissatisfaction_rate.svg`
- `top_customer_states.svg`
- `payment_method_distribution.svg`
- `seller_revenue_concentration.svg`

## Headline Results

- Total orders: **99,441**
- Delivered orders: **96,478**
- Total revenue: **15,843,553.24**
- Average order value: **159.33**
- Repeat customer share: **3.1%**
- Average review score: **4.09**
- Average delivery time: **12.6 days**
- Late delivery rate: **7.9%**

## Key Business Insights

- Late delivery is strongly associated with low customer review scores.
- Repeat customer share is low, which creates a clear retention opportunity.
- Revenue is led by categories such as health and beauty, watches and gifts, bed bath table, sports leisure, and computers accessories.
- Customer demand is concentrated in major states such as SP, RJ, and MG.
- Credit card is the dominant payment method, while boleto remains an important secondary method.
- Seller revenue is distributed across many sellers, reducing dependency on only a small group of top sellers.

## Re-run Report Artifacts

To regenerate the report and visual outputs:

```bash
python3 build_report_artifacts.py
```
