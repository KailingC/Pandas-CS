#1 rename columns
#rename some of the  columns
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
#rename all the columns
df.columns = ['a', 'b']
