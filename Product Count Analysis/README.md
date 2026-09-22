# Product Count Analysis

## Overview

This task focuses on counting unique products by category using the Superstore dataset and identifying the category with the largest number of products.

## Objective

- Count unique products for each product category.
- Practice using Excel `COUNTIF` functions.
- Identify the category with the highest product count.
- Present the results in a clear and organized table.

## Dataset

**Dataset:** Superstore

The analysis uses the following fields:

- Product Name
- Category

Duplicate product entries were removed so that products were counted uniquely.

## Tools Used

- Microsoft Excel

## Methodology

1. Imported the Superstore dataset into Excel.
2. Selected the Product Name and Category columns.
3. Removed duplicate product-category combinations.
4. Created a product count table for:
   - Furniture
   - Office Supplies
   - Technology
5. Used the `COUNTIF` function to calculate the product count for each category.
6. Used Excel formulas to identify the category with the largest product count.
7. Organized and formatted the final results.

## Excel Formula

The product count was calculated using:

`=COUNTIF($B:$B,D2)`

The largest product count was identified using:

`=MAX(E2:E4)`

The corresponding largest category was identified using:

`=INDEX(D2:D4,MATCH(MAX(E2:E4),E2:E4,0))`

## Deliverables

- Product Count Analysis Excel file
- Product count table
- Largest category identification

## Key Learning

This task provided practical experience with Excel `COUNTIF`, duplicate removal, data organization, and basic category-level analysis.

## Author

**Palvai Deepika**
