import json

with open ('api_keys.json', 'r') as f:
    api_config = f.read()
api_config = json.loads(api_config)

#configs
retry_attempts = 2
request_timeout = 10
