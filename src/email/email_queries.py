import requests
import config
import json

class email_queries():
    def __init__(self, email):
        self.email = email
        self.breach_directory_key = config.api_config['api']['breach_directory']['key']
        self.breach_directory_url = config.api_config['api']['breach_directory']['url']
        self.breach_directory_host = config.api_config['api']['breach_directory']['host']
        self.email_rep_key = config.api_config['api']['email_rep']['key']
        self.email_rep_url = config.api_config['api']['email_rep']['url']

    def email_rep(self):
        api_url = self.email_rep_url + self.email
        headers = {
            "Key": self.email_rep_key,
            "User-Agent": "Investigation Toolbox"
        }
        r = requests.request(method="GET", url=api_url, headers=headers, timeout=config.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text