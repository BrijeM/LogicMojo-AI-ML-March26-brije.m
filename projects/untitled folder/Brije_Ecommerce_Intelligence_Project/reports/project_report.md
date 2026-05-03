# Brije Ecommerce Intelligence Project Report

## Project Title

Brije Ecommerce Intelligence Project: Customer, Revenue, Product, Seller, and Satisfaction Analytics

## Business Problem Statement

The business needs a clear view of marketplace performance across customers, orders, products, sellers, payments, delivery, and reviews. The goal of this project is to combine raw e-commerce datasets into an analytical view that helps identify revenue drivers, customer behavior patterns, operational bottlenecks, and satisfaction risks. These insights can support decisions around category focus, seller management, customer retention, payment strategy, and delivery improvement.

## Dataset Description

The project uses multiple relational e-commerce datasets stored in the dataset/ folder:

- orders.csv: 99,441 orders with order status and purchase, approval, shipping, delivery, and estimated delivery timestamps.
- order_item.csv: 112,650 order-item records with product, seller, price, freight value, and shipping limit details.
- payments.csv: 103,886 payment records with payment type, installments, and payment value.
- reviews.csv: 104,719 review records with review score, comments, and review timestamps.
- products.csv: 32,951 product records with category, description, photo, weight, and size attributes.
- customers.csv: 99,441 customer records with unique customer IDs and customer location details.
- sellers.csv: 3,095 seller records with seller city and state.
- location.csv: 1,000,163 geolocation records by zip-code prefix.
- category_translation.csv: 70 category translation records mapping original category names to English labels.

The data covers orders purchased from September 4, 2016 through October 17, 2018.

## Methodology

- Loaded and inspected all source datasets to understand record counts, columns, data types, missing values, duplicates, and key relationships.
- Cleaned and prepared the data by converting timestamp columns to datetime format, validating numeric fields, removing duplicate records where needed, and standardizing analysis-ready fields.
- Integrated the datasets using common keys such as order_id, customer_id, product_id, seller_id, and product_category_name.
- Engineered business features including total order value, item count, delivery days, late delivery flag, purchase month, customer repeat status, customer value, category revenue, seller revenue, and dissatisfaction indicators.
- Performed exploratory data analysis across customer behavior, revenue trends, product categories, seller contribution, payment preferences, delivery performance, and review scores.
- Summarized findings into business recommendations focused on growth, retention, logistics, and customer satisfaction.

## Key Findings

- The marketplace processed 99,441 total orders, of which 96,478 were delivered.
- Total item-plus-freight revenue was 15,843,553.24, with an average order value of 159.33.
- Repeat customer share was only 3.1%, indicating a large opportunity to improve retention and loyalty.
- Average review score was 4.09, showing generally positive customer satisfaction, but dissatisfaction is highly connected to delivery performance.
- Average delivery time was 12.6 days, and 7.9% of orders were delivered after the estimated delivery date.
- Late delivery is a major satisfaction risk: dissatisfied reviews, defined as review scores of 1 or 2, occurred in 52.9% of late deliveries compared with 11.3% of on-time or early deliveries.
- The highest revenue categories were health and beauty, watches and gifts, bed bath table, sports leisure, and computers accessories.
- The highest item-volume categories were bed bath table, health and beauty, sports leisure, furniture decor, and computers accessories.
- Customer demand was geographically concentrated, with the largest unique-customer states being SP, RJ, MG, RS, and PR.
- Credit card was the dominant payment method at 73.9% of payment records, followed by boleto at 19.0%.
- Revenue was distributed across many sellers: the top 10 sellers contributed 12.8% of total seller revenue, suggesting the marketplace is not overly dependent on a small seller group.

## Business Insights

- Delivery reliability is one of the strongest controllable drivers of customer satisfaction. Late orders show a much higher low-rating rate than on-time or early orders.
- The platform has strong acquisition but weak repeat behavior. Most customers purchase once, so retention programs can create meaningful incremental revenue.
- Revenue and demand are concentrated in a few leading product categories, making category-level merchandising and inventory planning important for growth.
- Demand is geographically concentrated in major states, especially SP, RJ, and MG, which can guide regional logistics planning and marketing allocation.
- Seller revenue is broad-based rather than dominated by only a few sellers, so marketplace health depends on improving the performance of a wide seller base.
- Credit card usage dominates payments, but boleto remains large enough to keep as a priority payment option for customer accessibility.

## Recommendations

- Prioritize delivery reliability by monitoring late-delivery rates, carrier performance, and seller shipping-limit compliance.
- Create retention campaigns for first-time customers, especially in high-demand states and top product categories.
- Invest in inventory, merchandising, and promotions for high-performing categories such as health and beauty, watches and gifts, and bed bath table.
- Build seller scorecards that combine revenue, fulfillment speed, late delivery, review score, and cancellation behavior.
- Improve customer communication for orders at risk of delay to reduce dissatisfaction and protect review scores.
- Maintain credit-card optimization while continuing to support boleto customers, since both represent meaningful payment behavior.

## Visual Outputs

The following labeled and readable chart files are included in reports/figures/:

- monthly_revenue_trend.svg
- top_categories_by_revenue.svg
- review_score_distribution.svg
- delivery_dissatisfaction_rate.svg
- top_customer_states.svg
- payment_method_distribution.svg
- seller_revenue_concentration.svg
