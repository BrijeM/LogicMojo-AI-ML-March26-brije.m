# Brije Ecommerce Intelligence Project

This project analyzes e-commerce marketplace data to understand customer behavior, revenue performance, product demand, seller contribution, payment preferences, delivery performance, and customer satisfaction.

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
└── reports/
```

## Dataset Description

The project uses the following datasets:

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

## Required Final Deliverables

The final submission should include:

- Project report in PDF or DOC/DOCX format
- Project title
- Business problem statement
- Dataset description
- Methodology
- Key findings
- Business insights
- Recommendations
- Visual outputs with all key charts and graphs

## Headline Results

- Total orders: **99,441**
- Delivered orders: **96,478**
- Total revenue: **15,843,553.24**
- Average order value: **159.33**
- Repeat customer share: **3.1%**
- Average review score: **4.09**

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
