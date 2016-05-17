class ProbeCollapser (object):
    '''Collapses rows for probes from the same gene by averaging across the rows. E.g. Different Affy probes for the same
    Entrez identifier'''
    
    def __init__(self,Map_file,Data_file,Map_file_ref_col,Map_file_target_col,Data_file_key_col,Output_file):
        
        self.Map_file = Map_file
        self.Data_file = Data_file
        self.Map_file_ref_col = Map_file_ref_col
        self.Map_file_target_col = Map_file_target_col
        self.Data_file_key_col = Data_file_key_col
        self.Output_file = Output_file
        
    def Collapser(self):
        '''Function maps and collapses expression values for probes mapping to the same gene'''
        
        import pandas as pd
        
        assert self.Map_file.endswith('.csv')
        assert self.Data_file.endswith('.csv')
        assert self.Output_file.endswith('.csv')
        
        # Read in the two files as dataframes
        
        data_map = pd.read_csv(self.Map_file)
        mydata = pd.read_csv(self.Data_file)

        # Extract relevent columns from data_map
        
        data_map_cols = data_map[[self.Map_file_ref_col,self.Map_file_target_col]]

        #Do the mapping between the files

        Data_df = pd.DataFrame()

        for i in data_map_cols[self.Map_file_target_col]:
            new = mydata[mydata[self.Data_file_key_col] == i]
            Data_df = Data_df.append(new)

        Mapping_df = pd.DataFrame()

        for i in Data_df[self.Data_file_key_col]:
            newer = data_map_cols[data_map_cols[self.Map_file_target_col] ==i]
            Mapping_df = Mapping_df.append(newer)

        Mapping_df = Mapping_df.reset_index(drop = True)
        Data_df = Data_df.reset_index(drop = True)

        # Merge the two dataframes
        Merged_df = pd.concat([Mapping_df,Data_df], axis= 1).drop(self.Map_file_target_col, axis =1)

        Pruned_df = Merged_df.drop(self.Data_file_key_col,axis = 1).reset_index(drop = True)
        
        # Average out rows from the same reference id (e.g. same gene different probe ids)
        Pruned_df_ave = Pruned_df.reset_index(drop = True).groupby(self.Map_file_ref_col).mean()

        # Write csv file
        Pruned_df_ave.to_csv(self.Output_file)
        
        return("Run completed")


               
