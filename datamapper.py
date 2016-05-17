class DataMapper():
    '''Takes as input two dataframes. Uses the specified column values from the reference dataframe to find rows of the target dataframe where these values map to. Outputs
a dataframe containing the matched rows extracted from the target dataframe'''
    
    def __init__(self,ref_file_path, tar_file_path,ref_file_col,tar_file_col,output_path):
        self.ref_file_path = ref_file_path
        self.tar_file_path = tar_file_path
        self.ref_file_col = ref_file_col
        self.tar_file_col = tar_file_col
        self.output_path = output_path

    def datamap(self):
        
        import pandas as pd

        ## This is the file containing the column of identifiers to be mapped.E.g. Entrez ids.
        dataframe_ref = pd.read_csv(self.ref_file_path)
        assert ".csv" in self.ref_file_path

        ## This is the file containing the target data, a column of which will contain mappable data from the reference file.E.g. Expression data containing Entred ids.
        dataframe_tar = pd.read_csv(self.tar_file_path)
        assert ".csv" in self.tar_file_path

        ##This is the output dataframe
        dataframe_out = pd.DataFrame()

        for i in dataframe_ref[self.ref_file_col]:
            index = dataframe_tar[dataframe_tar[self.tar_file_col] == i].index.tolist()
            dataframe_out = dataframe_out.append(dataframe_tar.loc[index])
            
        dataframe_out.to_csv(self.output_path,index = False)
        assert ".csv" in self.output_path

        return "Data mapping completed and a new file has been generated"
    



        
        

