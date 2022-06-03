import requests
import docs.conf as conf
import json

class ip_queries():
    def __init__(self, ipv4):
        self.ipv4 = ipv4
        self.ipdb_key = conf.api_conf['api']['abuse_ipdb']['key']
        self.ipdb_url = conf.api_conf['api']['abuse_ipdb']['url']
        self.shodan_key = conf.api_conf['api']['shodan']['key']
        self.shodan_url = conf.api_conf['api']['shodan']['url']

    def abuse_ipdb(self):
        querystring = {
            'ipAddress': self.ipv4,
            'maxAgeInDays': '90'
        }
        headers = {
            'Accept': 'application/json',
            'Key': self.ipdb_key
        }
        r = requests.request(method='GET', url=self.ipdb_url, headers=headers, params=querystring, timeout=conf.request_timeout)
        r_text = json.dumps(r.json()['data'], sort_keys=False, indent=4)
        return r_text

    def shodan_ipv4(self):
        api_url = self.shodan_url + f"/shodan/host/{self.ipv4}?key={self.shodan_key}"
        r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text