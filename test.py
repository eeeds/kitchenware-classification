import requests

url = 'http://localhost:9696/predict'
#url = 'http://localhost:8080/predict'
data = {'url': 'https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/31OEvRveV3L.jpg'}

result = requests.post(url, json=data).json()
print(result)