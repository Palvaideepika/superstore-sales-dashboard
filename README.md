# 📊 Superstore Sales Dashboard

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Superstore dataset and presents the results through an interactive Streamlit dashboard.

The project was completed using free tools and resources.

## Objectives

- Understand the structure of the Superstore dataset
- Perform data quality checks
- Calculate summary statistics
- Analyze sales and profit
- Identify patterns and outliers
- Compare sales across categories and regions
- Create an interactive dashboard
- Deploy the dashboard online
- Document deployment and rollback procedures

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- GitHub

## Dataset

The project uses the Sample Superstore dataset containing sales, profit, product, category, customer, and regional information.

The dataset contains 9,994 records and 21 columns.

## EDA Approach

1. Loaded the Superstore dataset using Pandas.
2. Inspected the dataset structure and data types.
3. Checked for missing values and duplicate records.
4. Converted date columns into date format.
5. Generated summary statistics.
6. Analyzed sales and profit distributions.
7. Compared sales and profit across product categories.
8. Compared sales across regions.
9. Created visualizations using Matplotlib and Seaborn.
10. Developed an interactive Streamlit dashboard.

## Key Insights

- Technology is the strongest-performing category in terms of total sales.
- Technology also generates the highest total profit among the categories.
- Sales values are unevenly distributed, with some high-value orders.
- Regional sales performance differs across the business.
- The dashboard provides an easy way to explore sales and profit performance.

## Dashboard

The project includes an interactive Streamlit dashboard displaying:

- Total Sales
- Total Profit
- Total Orders
- Average Sales
- Sales by Category
- Profit by Category
- Sales by Region
- Dataset Preview
- Top 3 Business Insights

## Deployment

The application was successfully deployed using Streamlit Community Cloud.

**Live Dashboard:**

https://deepika-superstore-dashboard.streamlit.app/

## Deployment Evidence

Deployment verification is documented in:

`deployment_evidence.txt`

The file records the successful deployment and verification of the dashboard.

## Rollback Strategy

GitHub version control is used to maintain stable versions of the project.

If a deployment problem occurs:

1. Identify the previous stable commit.
2. Restore the stable version using Git.
3. Push the restored version to GitHub.
4. Redeploy the application.
5. Verify that the dashboard works correctly.

Rollback documentation is provided in:

`rollback_evidence.txt`

## Project Files

```text
superstore-sales-dashboard/
├── EDA_Superstore.ipynb
├── Sample - Superstore.csv
├── app.py
├── requirements.txt
├── README.md
├── config.toml
├── deployment_evidence.txt
└── rollback_evidence.txt
Superstore_Sales_Dashboard.pbix
