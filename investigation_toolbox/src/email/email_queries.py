import requests
import docs.conf as conf
import json

class email_queries():
    def __init__(self, email):
        self.email = email
        self.breach_directory_key = conf.api_conf['api']['breach_directory']['key']
        self.breach_directory_url = conf.api_conf['api']['breach_directory']['url']
        self.breach_directory_host = conf.api_conf['api']['breach_directory']['host']
        self.email_rep_key = conf.api_conf['api']['email_rep']['key']
        self.email_rep_url = conf.api_conf['api']['email_rep']['url']

    def email_rep(self):
        api_url = self.email_rep_url + self.email
        headers = {
            "Key": self.email_rep_key,
            "User-Agent": "Investigation Toolbox"
        }
        r = requests.request(method="GET", url=api_url, headers=headers, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text