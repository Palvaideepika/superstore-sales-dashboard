# Regional Growth Analysis

## 📌 Project Overview

This project analyzes sales growth across different regions over time using the Superstore dataset.

The objective is to compare regional sales performance, calculate year-over-year growth rates, identify high- and low-performing regions, and present the results using Excel visualizations and SQL analysis.

---

## 🎯 Objective

The main objectives of this project are:

- Analyze sales performance across different regions.
- Compare sales between different years.
- Calculate regional growth percentages.
- Identify regions with the highest and lowest growth.
- Understand changes in regional performance over time.
- Present the findings using tables and charts.

---

## 🛠️ Tools & Technologies

- **Microsoft Excel**
- **MySQL**
- **SQL**
- **Superstore Dataset**

---

## 📂 Dataset

The project uses the **Superstore Sales Dataset**.

Important columns used in the analysis:

- `Order Date`
- `Region`
- `Sales`

The `Order Date` column was used to extract the year, while `Region` and `Sales` were used to calculate regional sales and growth.

---

## 🔍 Analysis Process

### 1. Data Preparation

The Superstore dataset was loaded into Excel.

A new `Year` column was created from the `Order Date` column using:

```excel
=YEAR(A2)
