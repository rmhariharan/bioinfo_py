class DataMapper():
    '''Takes as input two dataframes. Uses the specified column values from the reference dataframe to find rows of the target dataframe where these values map to. Outputs
a dataframe containing the matched rows extracted from the target dataframe'''
    
    def __init__(self,Ref_file_path, Tar_file_path,Ref_file_col,Tar_file_col,Output_path):
        self.Ref_file_path = Ref_file_path
        self.Tar_file_path = Tar_file_path
        self.Ref_file_col = Ref_file_col
        self.Tar_file_col = Tar_file_col
        self.Output_path = Output_path

    def dataMap(self):
        
        import pandas as pd

        ## This is the file containing the column of identifiers to be mapped.E.g. Entrez ids.
        dataframe_ref = pd.read_csv(self.Ref_file_path)
        assert ".csv" in self.Ref_file_path

        ## This is the file containing the target data, a column of which will contain mappable data from the reference file.E.g. Expression data containing Entred ids.
        dataframe_tar = pd.read_csv(self.Tar_file_path)
        assert ".csv" in self.Tar_file_path

        ##This is the output dataframe
        dataframe_out = pd.DataFrame()

        for i in dataframe_ref[self.Ref_file_col]:
            index = dataframe_tar[dataframe_tar[self.Tar_file_col] == i].index.tolist()
            dataframe_out = dataframe_out.append(dataframe_tar.loc[index])
            
        dataframe_out.to_csv(self.Output_path,index = False)
        assert ".csv" in self.Output_path

        print("Data mapping completed and a new file has been generated")
    



        
        

