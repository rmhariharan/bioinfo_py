class ProbeCollapser (object):
    '''Collapses rows for probes from the same gene by averaging across the rows. E.g. Different Affy probes for the same
    Entrez identifier'''
    
    def __init__(self,map_file,data_file,map_file_ref_col,map_file_target_col,data_file_key_col,output_file):
        
        self.map_file = map_file
        self.data_file = data_file
        self.map_file_ref_col = map_file_ref_col
        self.map_file_target_col = map_file_target_col
        self.data_file_key_col = data_file_key_col
        self.output_file = output_file
        
    def collapser(self):
        '''Function maps and collapses expression values for probes mapping to the same gene'''
        
        import pandas as pd
        
        assert self.map_file.endswith('.csv')
        assert self.data_file.endswith('.csv')
        assert self.output_file.endswith('.csv')
        
        # Read in the two files as dataframes
        
        data_map = pd.read_csv(self.map_file)
        mydata = pd.read_csv(self.data_file)

        # Extract relevent columns from data_map
        
        data_map_cols = data_map[[self.map_file_ref_col,self.map_file_target_col]]

        #Do the mapping between the files

        data_df = pd.DataFrame()

        for i in data_map_cols[self.map_file_target_col]:
            new = mydata[mydata[self.data_file_key_col] == i]
            data_df = data_df.append(new)

        mapping_df = pd.DataFrame()

        for i in data_df[self.data_file_key_col]:
            newer = data_map_cols[data_map_cols[self.map_file_target_col] ==i]
            mapping_df = mapping_df.append(newer)

        mapping_df = mapping_df.reset_index(drop = True)
        data_df = data_df.reset_index(drop = True)

        # Merge the two dataframes
        merged_df = pd.concat([mapping_df,data_df], axis= 1).drop(self.map_file_target_col, axis =1)

        pruned_df = merged_df.drop(self.data_file_key_col,axis = 1).reset_index(drop = True)
        
        # Average out rows from the same reference id (e.g. same gene different probe ids)
        pruned_df_ave = pruned_df.reset_index(drop = True).groupby(self.map_file_ref_col).mean()

        # Write csv file
        pruned_df_ave.to_csv(self.output_file)
        
        return("Run completed")


               
