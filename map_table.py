import pandas as pd

from os import listdir
from os.path import isfile

# Obtain every expansion list
onlyfiles = [f for f in listdir('.') if isfile(f) and 'expansion' in f]
first = True

associator = {}
map_table = []

# For each initial target gene, we traduce the T****** name to the standard gene name
filtered = open('hgnc_cc_zero_filtered_anno.csv','r')
lines = [line for line in filtered.readlines()]
lines = lines[1:]
for line in lines:
    line_split = line.split(';')
    code_raw = line_split[4].split('@')
    if len(code_raw[0].split(',')) > 1:
        code_raw[0] = (code_raw[0].split(','))[0]
    code = code_raw[1] + '_' + code_raw[0]
    associator[line_split[0]] = code

ranger = [0.7]
# For each threshold...
for j in ranger:
    times = {}
    i = 0
    counter = 0
    map_table = []
    first = True

    # For each expansion list...
    for file in onlyfiles:
        previous = 1.0
        f = open(file, 'r')
        firstLine = True
        header = True
        lines = [line for line in f.readlines()]
        line_rows = []
        line_cols = []
        name = associator.get((lines[0].split(" "))[3].split("-")[0].strip(), (lines[0].split(" "))[3].split("-")[0].strip())
        dictionary = {name: []}
        print name

        # For each expanded gene inside the file
        for line in lines[2:]:
            line_split = line.split(',')

            # Stop the scan of the file if the relative frequency is lower than our threshold
            if float(line_split[3]) < j:
                print "STOP ON" + str(float(line_split[3]))
                break
            # Translate T****** name with standard gene names
            if times.get(associator.get(line_split[1].replace('t', 'T'), line_split[1].replace('t', 'T')), 0):
                times[associator.get(line_split[1].replace('t', 'T'), line_split[1].replace('t', 'T'))] += 1
            else:
                times[associator.get(line_split[1].replace('t', 'T'), line_split[1].replace('t', 'T'))] = 1
            line_rows.append(associator.get(line_split[1].replace('t', 'T'), line_split[1].replace('t', 'T')))
            dictionary[name].append(line_split[3])

        # Outer join of our results to build the final dataframe
        if first:
            first = False
            df = pd.DataFrame(dictionary, index=line_rows)
            map_table = df
            i += len(dictionary[name])
        else:
            df = pd.DataFrame(dictionary, index=line_rows)
            map_table = map_table.join(df, how='outer')
            i += len(dictionary[name])
    columns = list(map_table)
    # Replace NaN with 0s
    map_table = map_table.fillna(0)
    map_table.to_csv('map_table_' + str(j) + '.csv')

