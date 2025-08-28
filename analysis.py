# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("myntra_womens_dresses_clean.csv")
os.makedirs("figures", exist_ok=True)

# Descriptive stats
print(df[["MRP","Discounted Price","Discount %","Rating"]].describe())
print("\nTop brands by product count:\n", df["Brand"].value_counts().head(5))
print("\nAvg discount % by brand:\n", df.groupby("Brand")["Discount %"].mean().sort_values(ascending=False).head(5))

# Histogram of prices
plt.figure()
sns.histplot(df["Discounted Price"].dropna(), bins=30, kde=True)
plt.title("Distribution of Discounted Price (₹)")
plt.xlabel("Discounted Price (₹)")
plt.ylabel("Count")
plt.savefig("figures/hist_discounted_price.png")
plt.close()

# Average discount % by brand (top 10)
avg_discount_top = df.groupby("Brand")["Discount %"].mean().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=avg_discount_top.values, y=avg_discount_top.index, orient='h')
plt.title("Average Discount % by Top Brands")
plt.xlabel("Avg Discount %")
plt.ylabel("Brand")
plt.savefig("figures/bar_avg_discount_by_brand.png")
plt.close()

# Box plot – discounted price
plt.figure()
sns.boxplot(x=df["Discounted Price"].dropna())
plt.title("Box Plot – Discounted Price Distribution")
plt.xlabel("Discounted Price (₹)")
plt.savefig("figures/box_discounted_price.png")
plt.close()

# Scatter – Ratings vs Discount %
plt.figure()
sns.scatterplot(data=df, x="Discount %", y="Rating", alpha=0.6)
plt.title("Discount % vs Rating")
plt.xlabel("Discount %")
plt.ylabel("Rating")
plt.savefig("figures/scatter_discount_vs_rating.png")
plt.close()

print("\n✅ Analysis, visualizations saved to ./figures")
