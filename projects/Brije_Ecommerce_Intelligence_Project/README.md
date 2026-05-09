# Brije Ecommerce Intelligence Project

This project analyzes e-commerce marketplace data to understand customer behavior, revenue performance, product demand, seller contribution, payment preferences, delivery performance, and customer satisfaction. The final output is a business-focused intelligence report with charts, insights, and recommendations.

## Project Objective

The objective is to convert raw e-commerce data into useful business insights and recommendations. The analysis focuses on identifying revenue drivers, operational issues, customer satisfaction patterns, and opportunities for growth and retention.

## Repository Structure

```text
Brije_Ecommerce_Intelligence_Project/
├── README.md
├── ecommerce_project.ipynb
├── dataset/
│   ├── category_translation.csv
│   ├── customers.csv
│   ├── location.csv
│   ├── order_item.csv
│   ├── orders.csv
│   ├── payments.csv
│   ├── products.csv
│   ├── reviews.csv
│   └── sellers.csv
├── guidelines/
│   └── project_guidelines_problem_statement.docx
├── reports/
│   └── project_report.pdf
└── scripts/
    └── convert_docx_to_pdf.py
```

## Dataset Description

The project uses the following relational e-commerce datasets:

- `orders.csv`: order status and order timeline details
- `order_item.csv`: item-level order details including product, seller, price, and freight value
- `payments.csv`: payment type, installments, and payment value
- `reviews.csv`: customer review scores and review comments
- `products.csv`: product category and product dimension information
- `customers.csv`: customer IDs and customer location details
- `sellers.csv`: seller IDs and seller location details
- `location.csv`: geolocation details by zip-code prefix
- `category_translation.csv`: product category translations to English

## Notebook Workflow

The main analysis is completed in `ecommerce_project.ipynb` and covers:

- Data loading and initial exploration
- Data cleaning and preprocessing
- Data integration across multiple tables
- Feature engineering
- Exploratory data analysis
- Customer analysis
- Revenue and order analysis
- Product category analysis
- Seller analysis
- Review and satisfaction analysis
- Business insights and recommendations

## Final Deliverables

The final project deliverables are:

- `reports/project_report.pdf`: final report with the problem statement, dataset description, methodology, findings, insights, recommendations, and visual outputs.
- `ecommerce_project.ipynb`: complete analysis notebook used to prepare the report.
- `scripts/convert_docx_to_pdf.py`: helper script for converting a Word report to PDF when a DOCX version is available.

## Headline Results

- Total orders: **99,441**
- Delivered orders: **96,478**
- Total revenue: **15,843,553.24**
- Average order value: **159.33**
- Repeat customer share: **3.1%**
- Average review score: **4.09**

## Visual Outputs

The report includes visual analysis for:

- New vs repeat customers
- Customer value segments
- Geographic distribution of customers
- Monthly revenue trends
- Monthly order volume trends
- Peak sales periods
- Top-selling product categories
- Revenue contribution by category
- Product demand distribution
- Top-performing sellers
- Seller revenue contribution
- Seller distribution by state
- Review score distribution
- Delivery time and review ratings
- Dissatisfaction patterns
- Correlation heatmap for order-level metrics

## Key Business Insights

- Late delivery has a strong negative relationship with customer satisfaction.
- Repeat customer share is low, which indicates an opportunity for retention campaigns.
- Revenue is concentrated in high-performing categories such as health and beauty, watches and gifts, bed bath table, sports leisure, and computers accessories.
- Customer demand is concentrated in major states such as SP, RJ, and MG.
- Credit card is the most-used payment method, while boleto remains an important alternative.
- Seller revenue is distributed across many sellers, reducing dependence on only a few top sellers.

## Recommendations

- Improve delivery reliability and monitor late-delivery risk closely.
- Build retention campaigns for first-time customers.
- Prioritize inventory and promotions for high-revenue categories.
- Track seller performance using revenue, delivery, and review metrics together.
- Improve customer communication for delayed or at-risk orders.

## How to Use

1. Open `ecommerce_project.ipynb`.
2. Run the notebook cells from top to bottom.
3. Review the generated analysis, charts, insights, and recommendations.
4. Open `reports/project_report.pdf` for the final submitted report.

## PDF Conversion

If a DOCX report is available and needs to be converted again, run:

```bash
python3 scripts/convert_docx_to_pdf.py reports/project_report.docx reports/project_report.pdf
```

The script first attempts high-fidelity conversion with LibreOffice or Pages automation. A basic Python fallback can be used only when an approximate PDF is acceptable:

```bash
python3 scripts/convert_docx_to_pdf.py reports/project_report.docx reports/project_report.pdf --fallback
```
