import requests

#url = 'http://localhost:9696/predict'
#url = 'http://localhost:8080/predict'
url = 'http://aa56c022c1c1e4a3c9b98e0be0a19a55-546464646.us-east-1.elb.amazonaws.com/predict'
data = {'url': 'https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/31OEvRveV3L.jpg'}

result = requests.post(url, json=data).json()
print(result)