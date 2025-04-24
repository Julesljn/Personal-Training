import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AAPL_stock_data.csv")

print("Colonnes disponibles :", df.columns.tolist())
print("\nAperçu des 20 premières lignes :\n")
print(df.head(20))
