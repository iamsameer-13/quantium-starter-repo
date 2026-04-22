import pandas as pd
import glob
files = glob.glob("data/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].str.replace("$", "").astype(float)
df["sales"] = df["quantity"]*df["price"]
df = df[["sales","date","region"]]
df.to_csv("output.csv", index=False)
print("Done! output.csv created sucessfully!")
print(df.head())