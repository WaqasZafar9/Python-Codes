import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'John'],
    'Age': [28, 24, 35, 32, 28],
    'Country': ['USA', 'UK', 'Australia', 'Germany', 'USA']
}

df = pd.DataFrame(data)
print(df.head(5))
print(df.tail(5))
print(df.dtypes)
#methode no 2