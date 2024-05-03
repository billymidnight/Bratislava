import pandas as pd

df = pd.read_csv('your_file.csv')  

y = 100

df['x'] = y * (100 / (-df['udogsodds'])) / (df['favodds'] / 100)

df['giftreward'] = df['x'] * (df['favodds'] / 100) - y

df['standardized_giftreward'] = df['giftreward'] / df['x']
df_sorted_by_standardized = df.sort_values(by='standardized_giftreward', ascending=False)

top_10_standardized = df_sorted_by_standardized.head(10)

output_with_standardized = top_10_standardized[['betname', 'favodds', 'udogsodds', 'standardized_giftreward']]
print(output_with_standardized)
