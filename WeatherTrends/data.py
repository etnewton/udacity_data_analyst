import pandas as pd

data_sets = ['global.csv', 'louisville.csv', 'indianapolis.csv', 'nashville.csv']
data = []

for file in data_sets:
    data.append(pd.read_csv(file, index_col='year'))

data[0]['avg_temp'] = data[0]['avg_temp']

data_j = data[0].join(data[1][['avg_temp']], how='inner', rsuffix="_louisville")

# data_j = data_j.join(data[2][['avg_temp']], how='inner', rsuffix="_indy")
# data_j = data_j.join(data[3][['avg_temp']], how='inner', rsuffix="_nashville")

ten_avg = data_j.rolling(10, min_periods=1).mean()
quarter_century_avg = data_j.rolling(25, min_periods=1).mean()
century_avg = data_j.rolling(100, min_periods=1).mean()

print(data_j.rolling(100))

difference = (century_avg.rolling(2).apply(lambda x: x.iloc[1] - x.iloc[0])).rolling(100, min_periods=1).mean()

data_j = data_j.join(ten_avg, rsuffix="_10y_avg")
data_j = data_j.join(quarter_century_avg, rsuffix="_25y_avg")
data_j = data_j.join(century_avg, rsuffix="_100y_avg")
data_j = data_j.join(difference, rsuffix="_100y_delta")
(data_j["avg_temp_louisville_100y_avg"] - data_j["avg_temp_100y_avg"]).to_csv('difference_data.csv')
# data_j.to_csv('processed_data.csv')