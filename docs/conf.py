import json

#API Keys
with open ('api_keys.json', 'r') as f:
    api_conf = f.read()
api_conf = json.loads(api_conf)

#Request variables
retry_attempts = 2
request_timeout = 10
