import requests
import config
import json
from datetime import datetime

def logger(input_data):
  current_date = datetime.today().strftime('%Y-%m-%d')
  current_time = datetime.today().strftime('%H:%M:%S')
  with open(f"logs\error_log-{current_date}.txt", "a") as f:
    f.write(f"{current_time} | {input_data}\n")
  f.close()

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

    def breach_directory(self):
        querystring = {
            "func":
                "sources",
                "term": self.email
        }
        headers = {
            'X-RapidAPI-Host': self.breach_directory_host,
            'X-RapidAPI-Key': self.breach_directory_key
        }
        r = requests.request(method="GET", url=self.breach_directory_url, headers=headers, params=querystring, timeout=config.request_timeout)
        r_text = json.dumps(r.json()['sources'], sort_keys=False, indent=4)
        return r_text

class ip_queries():
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.ipdb_key = config.api_config['api']['abuse_ipdb']['key']
        self.ipdb_url = config.api_config['api']['abuse_ipdb']['url']

    def abuse_ipdb(self):
        querystring = {
            'ipAddress': self.ipv4,
            'maxAgeInDays': '90'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.ipdb_key
        }
        r = requests.request(method='GET', url=self.ipdb_url, headers=headers, params=querystring, timeout=config.request_timeout)
        r_text = json.dumps(r.json()['data'], sort_keys=False, indent=4)
        return r_text

class host_queries():
    def __init__(self, hostname):
        self.hostname = hostname
        self.whois_lookup_key = config.api_config['api']['whois_lookup']['key']
        self.whois_lookup_url = config.api_config['api']['whois_lookup']['url']

    def whois_lookup(self):
        querystring = {
            "key": self.whois_lookup_key,
            "domain": self.hostname,
            "format": "json"
        }
        r = requests.request(method="GET", url=self.whois_lookup_url, params=querystring, timeout=config.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text