import requests
from datetime import datetime, timedelta

date_one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
period = 1

url = "https://api.carbonintensity.org.uk/intensity/date/{date}/{period}"
# Update the URL with the date and period
url = url.format(date=date_one_year_ago, period=period)

headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
print(response.json())