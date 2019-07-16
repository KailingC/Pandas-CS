#1
#Datetime data to day, week, year, hour...
train['Year'] = train.Dates.dt.year#.dt.year


#2
#Convert String to datetime
pd.to_datetime('string of date')
