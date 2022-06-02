import requests
import docs.conf as conf
import json

class host_queries():
    def __init__(self, hostname):
        self.hostname = hostname
        self.whois_lookup_key = conf.api_conf['api']['whois_lookup']['key']
        self.whois_lookup_url = conf.api_conf['api']['whois_lookup']['url']
        self.shodan_key = conf.api_conf['api']['shodan']['key']
        self.shodan_url = conf.api_conf['api']['shodan']['url']

    def whois_lookup(self):
        querystring = {
            "key": self.whois_lookup_key,
            "domain": self.hostname,
            "format": "json"
        }
        r = requests.request(method="GET", url=self.whois_lookup_url, params=querystring, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text
    
    def shodan_host(self):
        api_url = self.shodan_url + f"/shodan/host/search?key={self.shodan_key}&query={self.hostname}"
        r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text