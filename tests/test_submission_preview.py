import pandas as pd

df = pd.read_csv(
    "submission.csv"
)

print(df.head(20))
print("\nRows:", len(df))