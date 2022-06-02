import json

#API Keys
with open ('api_keys.json', 'r') as f:
    api_conf = f.read()
api_conf = json.loads(api_conf)

#Request variables
retry_attempts = 2
request_timeout = 10

#Output strings
result = "#" * 120 + "\n" + "#" * 48 + " " * 8 + " Result " + " " * 8 + "#" * 48 + "\n" + "#" * 120