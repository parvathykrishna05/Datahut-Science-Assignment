import pandas as pd

df = pd.read_csv("myntra_womens_dresses_raw.csv")
print("Before cleaning:", df.shape)

# Remove duplicates
df.drop_duplicates(subset=["Product URL"], inplace=True)

# Clean brand names
df["Brand"] = df["Brand"].str.strip().str.title()

# Numeric conversion
df["MRP"] = pd.to_numeric(df["MRP"], errors="coerce")
df["Discounted Price"] = pd.to_numeric(df["Discounted Price"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Number of Reviews"] = pd.to_numeric(df["Number of Reviews"], errors="coerce")

# Calculate discount %
df["Discount %"] = ((df["MRP"] - df["Discounted Price"]) / df["MRP"]) * 100
df["Discount %"] = pd.to_numeric(df["Discount %"], errors="coerce").round(2)

df.to_csv("myntra_womens_dresses_clean.csv", index=False, encoding="utf-8-sig")
print("After cleaning:", df.shape)
print("✅ Cleaned dataset saved as myntra_womens_dresses_clean.csv")
