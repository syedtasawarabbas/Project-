import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

df.dropna(iplace=True)
df.columns = [col.strip().lower().replace('','_')for col in df.columns]

df.to_csv("cleaned1_data.csv",index=False)

print("Data cleaned and saved")
