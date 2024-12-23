import pandas as pd

def display_csv_as_table(file_path):

    df = pd.read_csv(file_path)

    df['Year'] = pd.to_datetime(df['DATETIME']).dt.year
    EstimateData = df[df['Year'] <= 2023]
    TestData = df[df['Year'] == 2024]

    print("EstimateData:")
    print(EstimateData)
    print("\nTestData:")
    print(TestData)

file_path = 'Historic_23_12_2024_1337.csv'
display_csv_as_table(file_path)