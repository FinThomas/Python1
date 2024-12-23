import requests
from datetime import datetime, timedelta

# Calculate the date for 1 year ago
date_one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

# Define the period
period = 1

# Define the URL and headers
url = "https://api.carbonintensity.org.uk/intensity/date/{date}/{period}"
# Update the URL with the date and period
url = url.format(date=date_one_year_ago, period=period)

headers = {
    'Accept': 'application/json'
}


# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())