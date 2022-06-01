import requests
import docs.conf as conf
import json

class host_queries():
    def __init__(self, hostname):
        self.hostname = hostname
        self.whois_lookup_key = conf.api_conf['api']['whois_lookup']['key']
        self.whois_lookup_url = conf.api_conf['api']['whois_lookup']['url']

    def whois_lookup(self):
        querystring = {
            "key": self.whois_lookup_key,
            "domain": self.hostname,
            "format": "json"
        }
        r = requests.request(method="GET", url=self.whois_lookup_url, params=querystring, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text