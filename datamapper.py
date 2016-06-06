
    '''A module that takes as input two dataframes. Uses the specified column values from the reference dataframe to find rows of the target dataframe where these values map to. Outputs
a dataframe containing the matched rows extracted from the target dataframe'''
    
import pandas as pd

def dataMap(Ref_file_path, Tar_file_path,Ref_file_col,Tar_file_col,Output_path):
    
    ## This is the file containing the column of identifiers to be mapped.E.g. Entrez ids.
    dataframe_ref = pd.read_csv(Ref_file_path)
    assert ".csv" in Ref_file_path

    ## This is the file containing the target data, a column of which will contain mappable data from the reference file.E.g. Expression data containing Entred ids.
    dataframe_tar = pd.read_csv(Tar_file_path)
    assert ".csv" in Tar_file_path

    ##This is the output dataframe
    dataframe_out = pd.DataFrame()

    for i in dataframe_ref[Ref_file_col]:
        index = dataframe_tar[dataframe_tar[Tar_file_col] == i].index.tolist()
        dataframe_out = dataframe_out.append(dataframe_tar.loc[index])
        
    dataframe_out.to_csv(Output_path,index = False)
    assert ".csv" in Output_path

    return "Data mapping completed and a new file has been generated"
    



        
        

