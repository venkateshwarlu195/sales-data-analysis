# Sales Data Analysis Using Pandas and Matplotlib

## 📌 Project Overview
This project demonstrates how to use the Pandas library for data analysis and Matplotlib for data visualization. The analysis is performed on a sales dataset stored in a CSV file.

## 🛠 Technologies Used
- Python
- Pandas
- Matplotlib

## 📂 Project Structure
sales-data-analysis/
├── data/
|
│ └── sales_data.csv
|
├── outputs/
|
│ | 
| └── generated charts
|
├── src/
| |
│ └── analysis.py
|
├── README.md
|
├── requirements.txt

## 📊 Analysis Performed
- Data cleaning (currency formatting)
- Average sales amount calculation
- Average boxes shipped calculation
- Total sales by country (bar chart)
- Sales vs shipment volume (scatter plot)
- Correlation analysis (heatmap)
- Identification of top-selling product

## 📈 Visualizations
The following charts are generated and saved in the `outputs/` folder:
- Bar Chart: Total Sales by Country
- Scatter Plot: Sales Amount vs Boxes Shipped
- Heatmap: Correlation between sales and shipment volume

## ▶️ How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/venkateshwarlu195/sales-data-analysis.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3.Run the analysis:
```bash
python src/analysis.py
```
