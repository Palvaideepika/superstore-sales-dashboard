import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Superstore Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Superstore Sales Dashboard")
st.write("Interactive analysis of Superstore sales and profit data.")

# Load dataset
df = pd.read_csv(
    "Sample - Superstore.csv",
    encoding="latin1"
)
)

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Key metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Average Sales", f"${average_sales:,.2f}")

st.divider()

# Sales by Category
st.subheader("Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots()
category_sales.plot(kind="bar", ax=ax1)

ax1.set_xlabel("Category")
ax1.set_ylabel("Total Sales")
ax1.set_title("Total Sales by Category")

st.pyplot(fig1)

# Profit by Category
st.subheader("Profit by Category")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots()
category_profit.plot(kind="bar", ax=ax2)

ax2.set_xlabel("Category")
ax2.set_ylabel("Total Profit")
ax2.set_title("Total Profit by Category")

st.pyplot(fig2)

# Sales by Region
st.subheader("Sales by Region")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig3, ax3 = plt.subplots()
region_sales.plot(kind="bar", ax=ax3)

ax3.set_xlabel("Region")
ax3.set_ylabel("Total Sales")
ax3.set_title("Total Sales by Region")

st.pyplot(fig3)

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

# Top insights
st.subheader("Top 3 Insights")

st.write(
    "1. Technology generates the highest total sales among the product categories."
)

st.write(
    "2. Technology also generates the highest total profit."
)

st.write(
    "3. Regional sales performance differs, with the West region generating the highest sales."
)

st.success("Dashboard loaded successfully!")
