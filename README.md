Walmart Sales Data Analysis
This project uses Python and Pandas to analyze Walmart's historical sales data. The goal is to generate insights on store performance, holiday impact, and monthly sales trends.

📁 Dataset
File: Walmart_Sales.csv
Columns:
Column	Description
Store	Store ID
Date	Date of sales entry (e.g. 19-02-2010)
Weekly_Sales	Sales for the week
Holiday_Flag	1 = Holiday week, 0 = Non-holiday week
Temperature	Weekly average temperature
Fuel_Price	Fuel price in the region
CPI	Consumer Price Index
Unemployment	Regional unemployment rate

🧪 Objective
Analyze Walmart sales data using:
pandas for data processing
matplotlib for visualization

📌 Key Analysis Performed
✅ Total Sales by Store
✅ Monthly Sales Trends
✅ Holiday vs Non-Holiday Sales Comparison
✅ Basic statistics and data quality checks

📈 Visualizations
📊 Bar Chart: Total sales by store

📈 Line Chart: Monthly sales trend

🟣 Bar Chart: Average sales on holiday vs non-holiday weeks

🚀 How to Run
Clone the repository or download the .py file.
Ensure the Walmart_Sales.csv file is placed correctly.

Run the Python script:
python main.py

🛠️ Requirements
Python 3.7+
pandas
matplotlib

Install required packages:
pip install pandas matplotlib
📍 Sample Insights (Example)
Store 20 had the highest total sales.

Holiday weeks have slightly lower average sales than non-holidays.

Sales peak around November–December, indicating seasonal trends.

📚 Files
File	Description
main.py	Main Python analysis script
Walmart_Sales.csv	Input dataset (CSV format)
README.md	Project documentation
