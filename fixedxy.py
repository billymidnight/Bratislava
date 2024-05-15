import pandas as pd

# Define the constant value
x = 250

# Read the data
df = pd.read_csv('data.csv')

# Set df['y'] to 0 for all rows
df['y'] = 0

# Calculate sideval1 and sideval2 for each row using the constant value of y
df['sideval1'] = ((100/-df['favodds'])*df['y'] - x + 0.68*x).evalf()
df['sideval2'] = ((df['udogsodds'] / 100)*x - df['y'] + 0.68*df['y']).evalf()

# Sort the DataFrame in descending order of sideval1
df_sorted = df.sort_values(by='sideval1', ascending=False)

# Print the sorted DataFrame
print(df_sorted)
