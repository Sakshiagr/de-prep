# E-Commerce Sales ETL Pipeline

## Overview
End-to-end ETL pipeline processing 500,000+ real e-commerce 
transactions using Python and Pandas.

## Pipeline Steps
- **Extract**: Load raw data from CSV (541,909 records)
- **Transform**: 
  - Remove null CustomerIDs (135,080 rows)
  - Remove cancelled orders (8,905 rows)
  - Add TotalPrice column (Quantity × UnitPrice)
- **Analyse**:
  - Top 10 countries by revenue
  - Top 10 best selling products
- **Load**: Save cleaned data to CSV (397,924 records)

## Tech Stack
Python, Pandas, Git

## Results
- UK top country: £7.3M revenue
- Top product: Paper Craft Little Birdie (80,995 units)
