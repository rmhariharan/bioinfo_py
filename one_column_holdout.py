
def sample_holdout(input_file,output_file):
    '''From an input csv file with n columns (samples), creates files with all
       possible n-1 columns. Was written to check robustness of the PathWave algorithm'''
    
    import pandas as pd
    # Read in data from csv file
    data = pd.read_csv(input_file,index_col = 0)
    assert input_file.endswith(".csv")
    k =0
    for i in data:
        ColsToDrop = [data.columns[k]]
        newdata = data.drop(ColsToDrop,axis =1) ## Use the drop function to drop a column indexed by column name
        k =k+1
        newdata.to_csv(output_file+"/" + "newdata_minus_" + str(k) + ".csv")
    return "Completed"

