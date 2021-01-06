import pandas as pd
df = pd.read_csv("D:\\PyQt5_Sample\\Google\\구글트랜드.csv")

pd.plotting.scatter_matrix(df)