import pandas as pd

map_table = pd.read_csv('map_table_0_70_compressed_target.csv')
map_table2 = []

targets = map_table.columns
targets = targets[1:]
first = True

for target in targets:
    print target
    dictionary = {target: []}
    tmp = {}
    line_rows = []
    map2 = map_table[target]

    # For each gene in the rows of the map table...
    for i in range(1, len(map_table.index)):
        # We read the gene name, removing the isoform parameter.
        gene = map_table.iloc[i, 0]
        gene_split = gene.split('_')
        if gene_split[0] not in tmp:
            tmp[gene_split[0]] = [0, 0]

        # Take the higher relative frequency from all the gene isoforms.
        if map2.iloc[i] > 0:
            tmp[gene_split[0]][0] = max(map2.iloc[i],tmp[gene_split[0]][0])
            tmp[gene_split[0]][1] += 1
    for gene in tmp:
        # If no relative frequency was higher than zero, write zero; otherwise write the maximum relative frequency.
        if tmp[gene][1] == 0:
            dictionary[target].append(0.0)
        else:
            dictionary[target].append((tmp[gene][0]))
        line_rows.append(gene)

    # Iteratively outer join the resulting dataframe with new data
    if first:
        first = False
        df = pd.DataFrame(dictionary, index=line_rows)
        map_table2 = df
    else:
        df = pd.DataFrame(dictionary, index=line_rows)
        map_table2 = map_table2.join(df, how='outer')

map_table2.to_csv('map_table_0_70_all_compact.csv')
