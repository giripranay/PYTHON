import requests

URL="https://io.adafruit.com/api/v2/giripranay/feeds/bin1/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"


r = requests.get(url = URL)

data = r.json()

#for i in data:
#    print(i["value"])
print(data)

