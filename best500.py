import pandas as pd

df2 = pd.read_csv('map_table_cluster.csv')
first = True

# For each gene in map table count the target with a non-zero relative frequency, then sort in decreasing order.
df2['non zero'] = df2.gt(0).sum(axis=1) - 1
df = df2.sort_values(by='non zero', ascending=False)

# Write file with best 500 results
output = open('best500.txt', 'w')
for i in range(0, 500):
    output.write(df.iloc[i, 0] + "\n")

