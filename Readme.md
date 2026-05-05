# Sales Data Analysis Project (PRO)

## Overview
A comprehensive sales data analysis tool that processes sales transactions and generates actionable business insights with visualizations.

## Features
- **Sales Dashboard**: Displays key metrics (Total Revenue, Total Orders, Average Order Value)
- **Top Products Analysis**: Identifies best-selling products by revenue
- **Regional Performance**: Analyzes revenue by geographic regions
- **Category Distribution**: Shows sales breakdown by product category
- **Monthly Trends**: Visualizes sales trends over time
- **Automated Charts**: Generates 4 professional visualizations and saves them locally

## Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn

## Installation
```bash
pip install pandas matplotlib seaborn
```

## Usage
Run the script from the project directory:
```bash
python sales.py
```

The script will:
1. Load `sales_data.csv`
2. Process and calculate KPIs
3. Display a dashboard with key metrics
4. Generate and save 4 visualization charts to the `charts/` folder
5. Display all charts in windows

## Input Data Format
Expects a CSV file named `sales_data.csv` with the following columns:
```
Date,OrderID,Product,Quantity,Price,Region,Category
2024-01-01,001,Laptop,1,50000,North,Electronics
2024-01-02,002,Chair,3,5000,South,Furniture
...
```

## Output
- **Console Dashboard**: Sales metrics and insights
- **charts/top_products.png**: Bar chart of top products by revenue
- **charts/top_regions.png**: Bar chart of revenue by region
- **charts/monthly_sales.png**: Line chart showing monthly sales trends
- **charts/category_distribution.png**: Pie chart of sales by category

## Output Example
```
=============================================
📊 SALES ANALYSIS DASHBOARD
=============================================
Total Revenue       : ₹1,250,000
Total Orders        : 150
Average Order Value : ₹8,333.33

💡 Key Insights:
- Best selling product: Laptop
- Top performing region: North
- Highest revenue category: Electronics
```

## Notes
- All visualizations are automatically saved to the `charts/` folder
- The script uses Indian Rupee (₹) currency formatting
- Charts use seaborn styling for professional appearance
- File paths are resolved relative to the script location
