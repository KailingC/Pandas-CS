#1 rename columns
#rename some of the  columns
df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
#rename all the columns
df.columns = ['a', 'b']


#2 filter based on a list
df = df[df['subject_1'].isin([1, 2, 13, 18, 25])]
