import requests

url1 = "https://api.covid19india.org/v4/min/timeseries.min.json"
url2 = "http://api.open-notify.org/astros.json"
url3 = "http://api.open-notify.org/iss-pass.json"
# response = requests.get(url2)
# data = response.text

query_parameters = {'lat': '45', 'lon': '180'}
response = requests.get(url3, params=query_parameters)
data = response.json()
print(data)
print(type(data))

data_to_post = {'name': 'John', 'email': 'john@example.com'}
my_headers = {'anything': 'anything'}
response = requests.post("http://somehost/endpoint", data=data_to_post, headers=my_headers)

#Reference for API -> https://docs.zoop.one/#812757fa-0c32-4416-9d06-30ba89f381fc