import pandas as pd

df = pd.DataFrame ({ 'day': [1, 2, 3], 'user': [10, 20, 30]})

daily_users = df.groupby('day') \
    .agg({'user': 'max'})

print(daily_users)