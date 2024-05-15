import pandas as pd
from sympy import symbols, Eq, solve

udogsodds, favodds, y = symbols('udogsodds favodds y')
x = 250

equation = Eq((100/-favodds)*y - x + 0.68*x, (udogsodds / 100)*x - y + 0.68*y)

y_solution = solve(equation, y)[0]

# Read the data
df = pd.read_csv('data.csv')

#df['y'] = df.apply(lambda row: y_solution.subs({udogsodds: row['udogsodds'], favodds: row['favodds']}).evalf(), axis=1)
df['y'] = 0
df['sideval1'] = df.apply(lambda row: ((100/-row['favodds'])*row['y'] - x + 0.68*x).evalf(), axis=1)
df['sideval2'] = df.apply(lambda row: ((row['udogsodds'] / 100)*x - row['y'] + 0.68*row['y']).evalf(), axis=1)

df_sorted = df.sort_values(by='sideval1', ascending=False)

print(df_sorted)