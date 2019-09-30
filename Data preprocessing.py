# This file includes some useful codes of data preprocessing under Pandas

# Indicate the parameters for the datafile to retreive
code = "PDD"
timeseries='30 mins'

#define the directory of the historical data
path='/Users/...'  
filename=code+" "+timeseries+'.csv'
dayfilename=code+" "+'1 day'+'.csv'
stockdata=pd.read_csv(path+filename)

#convert the default date time format into independent date and time:
stockdata['Day']=pd.to_datetime(stockdata['date']).dt.date
stockdata['Hour']=pd.to_datetime(stockdata['date']).dt.hour
stockdata['Mins']=pd.to_datetime(stockdata['date']).dt.minute

#combine the close data with the minutes data by date
stockdaily=pd.read_csv(path+dayfilename)
Mdata=stockdaily[['close']]
Mdata.insert(0,'Day',pd.to_datetime(stockdaily['date']).dt.date)
...
