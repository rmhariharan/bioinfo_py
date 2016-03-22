## This program takes as input a .csv metadata file one column of which contains the identifiers for the data columns (samples)
## the second input .csv file is the actual data file. The code extracts sample columns whre coulmn headers match the metadata.

import pandas as pd

data = pd.read_csv(file1.csv)                       ## complete path to data file (.csv)
metadata = pd.read_csv(file2)        ## complete path to metadata file (.csv)

new = pd.DataFrame()
pos = 0
for i in metadata['']:                                                                     ## specify the column containing the identifiers to be matched
    x = str(i)
    extr_data = data.filter(regex = x)
    new.insert(pos,x,extr_data)
    pos = pos+1
new.to_csv(file3,sep = ',',header = True)     ## complete path to output file (.csv)
print("Done")


