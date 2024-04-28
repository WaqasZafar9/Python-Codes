import pandas as pd
df = pd.read_csv('autometa.csv')
print(df.head(5))
print(df.tail(5))
print(df.dtypes)