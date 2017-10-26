def decomp_ts(dataframe, series):
    datetime = pd.to_datetime(dataframe[series])
    dataframe['year'] = datetime.dt.year
    dataframe['month'] = datetime.dt.month
    dataframe['day'] = datetime.dt.day
    dataframe['dayofweek'] = datetime.dt.dayofweek
    dataframe['hour'] = datetime.dt.hour
    return dataframe