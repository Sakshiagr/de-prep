import pandas as pd

df = pd.read_csv("data.csv",encoding="latin1")
print("\n--- EXTRACT ---")
print("Raw Shape",df.shape)
print(df.head())
print(df.columns)
print(df.isnull().sum())

print("\n--- TRANSFORM ---")
df = df.dropna(subset = ["CustomerID"])
print("After Dropping nulls:", df.shape)
df["TotalPrice"] = df["Quantity"]*df["UnitPrice"]
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
print("After removing cancellation", df.shape)

print("\n--- ANALYSE ---")
top_countries = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)
print("Top 10 Countries by Revenue:")
print(top_countries)

top_products=df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
print("Top 10 Products by Quantity:")
print(top_products)

# Do this:
# df.groupby("Description")["Quantity"].sum()  # sums only Quantity ✅

print("\n--- LOAD ---")
df.to_csv("cleandata.csv", index=False)
print("ETL Pipeline completed successfully!")
print("Final dataset shaped",df.shape)