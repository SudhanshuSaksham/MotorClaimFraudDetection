import pandas as pd
import numpy as np

df = pd.read_csv("Dataset/PREPROCESSED/preprocessed.csv")
df_fraud = df.groupby(['policy_state'])
print(df_fraud['policy_annual_premium'].agg(np.size))

