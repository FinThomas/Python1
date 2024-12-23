import pandas as pd

def get_csv(file_path):

    df = pd.read_csv(file_path)

    df['Year'] = pd.to_datetime(df['DATETIME']).dt.year
    EstimateData = df[df['Year'] <= 2023]
    TestData = df[df['Year'] == 2024]
    
    return EstimateData, TestData

file_path = 'Historic_23_12_2024_1337.csv'

[EstimateData,TestData] = get_csv(file_path)

def average_annual_intensity(data):
    return data.groupby('Year')['CARBON_INTENSITY'].mean()

def average_monthly_intensity(data):
    data['Month'] = pd.to_datetime(data['DATETIME']).dt.month
    return data.groupby(['Year', 'Month'])['CARBON_INTENSITY'].mean()

def average_daily_intensity(data):
    data['Day'] = pd.to_datetime(data['DATETIME']).dt.day
    return data.groupby(['Year', 'Month', 'Day'])['CARBON_INTENSITY'].mean()

def average_hourly_intensity(data):
    data['Hour'] = pd.to_datetime(data['DATETIME']).dt.hour
    return data.groupby(['Year', 'Month', 'Day', 'Hour'])['CARBON_INTENSITY'].mean()


average_intensity = average_annual_intensity(EstimateData)
average_monthly_intensity = average_monthly_intensity(EstimateData)
average_daily_intensity = average_daily_intensity(EstimateData)
average_hourly_intensity = average_hourly_intensity(EstimateData)

print(average_intensity)
print(average_monthly_intensity)
print(average_daily_intensity)
print(average_hourly_intensity)

