import json

import requests

# Crashes
url = "https://www.data.gov.jm/api/3/action/package_show?id=1fe10db7-3a57-485d-bd60-98e5502e66c2"

try:
    response = requests.get(url)
    response.raise_for_status()

    json_data = response.json()
    print(json_data)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")

except ValueError as e:
    print(f"Error parsing JSON data: {e}")
