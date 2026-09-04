import pandas as pd

# 1. Chargement des données
df1 = pd.read_csv("data/orders.csv")
df2 = pd.read_csv("data/customers.csv")

# 2. Jointure
df = df1.merge(df2, on="customer_id", how="left")

# 3. Traitement des dates et conversion de types
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month
df["year_month"] = df["order_date"].dt.to_period("M")

# 4. Feature Engineering
df["total_price"] = df["unit_price"] * df["quantity"]
df["expensive"] = df["total_price"] > 1000

# 5. Capture des valeurs manquantes AVANT nettoyage
missing_before_clean = df.isna().sum()
unknown_orders_count = df["city"].isna().sum()

# 6. Nettoyage des valeurs manquantes
df["city"] = df["city"].fillna("Unknown")
df["name"] = df["name"].fillna("Unknown")

# 7. Agrégations et Analyses
ca_ville = df.groupby("city")["total_price"].sum().sort_values(ascending=False)
top3_villes = ca_ville.head(3)
ca_mensuel = df.groupby("year_month")["total_price"].sum()

# 8. Sauvegarde du dataset enrichi
df.to_csv("data/enriched_orders.csv", index=False)

# 9. Génération du rapport texte
with open("output/report.txt", "w") as f:
    f.write("======== SALES REPORT ========\n\n")

    f.write(f"Total Revenue: {df['total_price'].sum()}\n")
    f.write(f"Total Orders: {len(df)}\n")
    f.write(f"Average Order Value: {df['total_price'].mean()}\n\n")

    f.write("--- Revenue by City ---\n")
    f.write(f"{ca_ville}\n\n")

    f.write("--- Top 3 Cities ---\n")
    f.write(f"{top3_villes}\n\n")

    f.write("--- Revenue by Month ---\n")
    f.write(f"{ca_mensuel}\n\n")

    f.write("--- Data Quality & Missing Values ---\n")
    f.write(f"Initial Missing Values:\n{missing_before_clean}\n")
    f.write(f"Orders with unmatched customer profile: {unknown_orders_count}\n")