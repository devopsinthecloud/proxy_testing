import requests
username = "your_username"
password = "your_password"
PROXY_RACK_DNS = "your_proxy"
urlToGet = "http://ip-api.com/json"
proxy = {"http":"http://{}:{}@{}".format(username, password, PROXY_RACK_DNS)}
r = requests.get(urlToGet , proxies=proxy)
print("Response:\n{}".format(r.text))
