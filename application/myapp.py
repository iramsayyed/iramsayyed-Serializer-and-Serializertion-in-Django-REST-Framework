# ths fils act lika as third party and it can be anywhere
import requests
URL = 'http://127.0.0.1:8000/stuinfo/5'


# here r and data is verible which is anything
r = requests.get(url = URL)

data = r.json()
print(data)

# fullform of API(Application programming interface):
# it is basically a contract of service between two applications
# seprate third party app will be send a request to api to get data to use for app 