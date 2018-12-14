import pandas as pd

map_table = pd.read_csv('map_table_0_70.csv')
targets = list(map_table)
targets = targets[1:]
map_table2 = []


targets_noIso = {}
# First of all collect all target genes names
for target in targets:
    target_split = target.split('_')
    if targets_noIso.get(target_split[0], 0):
        targets_noIso[target_split[0]].append(target)
    else:
        targets_noIso[target_split[0]] = []
        targets_noIso[target_split[0]].append(target)

first = True
# For each initial target gene (not considering isoform)...
for target2 in targets_noIso:
    dictionary = {target2: []}
    line_rows = []

    # For each gene in the rows of the map table...
    for i in range(1, len(map_table.index)):
        # Read the gene name
        gene = map_table.iloc[i, 0]
        minimum = 1
        num = 0

        # For each isoform of the target gene we take its list...
        for isoforma in targets_noIso[target2]:
            lista = map_table[isoforma]
            # If its relative frequency is higher than zero for a gene we save the minimum value.
            if lista.iloc[i] > 0:
                minimum = min(lista.iloc[i], minimum)
                num += 1
        line_rows.append(gene)

        # If no relative frequency is higher than zero, we save 0 as final value.
        if num == 0:
            dictionary[target2].append(0)
        else:
            dictionary[target2].append(minimum)

    # If we are analyzing the first target gene, we create a new dataframe
    if first:
        first = False
        df = pd.DataFrame(dictionary, index=line_rows)
        map_table2 = df

    # Otherwise, we outer join the previous dataframe with our new data.
    else:
        df = pd.DataFrame(dictionary, index=line_rows)
        map_table2 = map_table2.join(df, how='outer')

map_table2.to_csv('map_table_0_70_compressed_target.csv')