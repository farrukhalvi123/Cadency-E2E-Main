import requests
import json

from requests.structures import CaseInsensitiveDict

mydata = open("data.json","r").read()
resp = requests.post("http://10.4.4.21:6225/v1/login",json=json.loads(mydata))
json_responce = resp.json()
print(resp.json)
print(resp.content)
print(resp.headers)
authtoken = json_responce["data"]["auth_token"]
print("&&&&&&&&&&", authtoken)
# print(json_responce["data"]["auth_token"])
# token1 = ["auth_token"]
# print("\n ***********",authtoken)
# userdata = open("UserData.json","r").read()
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(authtoken)}
resp = requests.get("http://10.4.4.21:6225/v1/users",headers= headers)
print(resp)
print(resp.content)
# print(resp.json)