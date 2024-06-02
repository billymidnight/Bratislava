import pandas as pd

df = pd.read_csv('data.csv')  

y = 200

df['x'] = (y * (100 / (-df['favodds'])) + y) / (1 + df['udogsodds'] / 100)
#print(df['x'])

df['giftreward'] = df['x'] * (df['udogsodds'] / 100) - y

df['standardized_giftreward'] = df['giftreward'] / df['x']
df_sorted_by_standardized = df.sort_values(by='standardized_giftreward', ascending=False)

top_10_standardized = df_sorted_by_standardized

output_with_standardized = top_10_standardized[['bname', 'favodds', 'udogsodds', 'giftreward', 'standardized_giftreward', 'x']]
print(output_with_standardized)