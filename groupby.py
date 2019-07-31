#1
#create dataframes based on each group in groups
gb = df.groupby('column')    
[gb.get_group(x) for x in gb.groups]
