import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression

df = pd.read_parquet(
    r"C:\uas-tbg\output\ml_visitor\ml_visitor.parquet"
)

X = df[["hour"]]
y = df["visitor_count"]

model = LinearRegression()

model.fit(X, y)

with open(
    r"C:\uas-tbg\output\visitor_model.pkl",
    "wb"
) as f:
    pickle.dump(model, f)

print("Model berhasil disimpan")