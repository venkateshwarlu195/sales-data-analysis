import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output directory
os.makedirs("../outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Clean Amount column
df["Amount"] = (
    df["Amount"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Basic analysis
avg_amount = df["Amount"].mean()
avg_boxes = df["Boxes Shipped"].mean()

print("Average Sales Amount:", avg_amount)
print("Average Boxes Shipped:", avg_boxes)

# ---------------------------
# Bar Chart: Total Sales by Country
# ---------------------------
sales_by_country = df.groupby("Country")["Amount"].sum()

plt.figure()
plt.bar(sales_by_country.index, sales_by_country.values)
plt.xlabel("Country")
plt.ylabel("Total Sales Amount")
plt.title("Total Sales by Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../outputs/sales_by_country.png")
plt.show()
plt.close()

# ---------------------------
# Scatter Plot: Amount vs Boxes Shipped
# ---------------------------
plt.figure()
plt.scatter(df["Boxes Shipped"], df["Amount"])
plt.xlabel("Boxes Shipped")
plt.ylabel("Sales Amount")
plt.title("Sales Amount vs Boxes Shipped")
plt.tight_layout()
plt.savefig("../outputs/amount_vs_boxes.png")
plt.show()
plt.close()

# ---------------------------
# Heatmap: Correlation
# ---------------------------
correlation = df[["Amount", "Boxes Shipped"]].corr()

plt.figure()
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation)), correlation.columns)
plt.yticks(range(len(correlation)), correlation.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("../outputs/correlation_heatmap.png")
plt.show()
plt.close()

# ---------------------------
# Top Product
# ---------------------------
top_product = df.groupby("Product")["Amount"].sum().idxmax()
print("Top-Selling Product:", top_product)
