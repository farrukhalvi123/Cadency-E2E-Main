import requests
import json
mydata = open("data.json","r").read()
resp = requests.post("http://10.4.4.21:6425/v1/login",json=json.loads(mydata))
json_responce = resp.json()
print(resp.json)
print(resp.content)
print(resp.headers)
authtoken = json_responce["data"]["auth_token"]
print(json_responce["data"]["auth_token"])

userdata = open("UserData.json","r").read()
resp = requests.put("http://10.4.4.21:6425/v1/user",json=json.loads(userdata), headers= {'Authorization': "Bearer {}".format(authtoken)})
print(resp)
print(resp.content)