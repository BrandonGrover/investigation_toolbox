import requests
import docs.conf as conf
import json
from time import sleep


class shodan():
    def __init__(self, **kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.shodan_key = conf.api_conf['api']['shodan']['key']
        self.shodan_url = conf.api_conf['api']['shodan']['url']

    def shodan_scan(self):
        if self.ipv4 is None:
            return "No IP address provided."
        status = ''
        query = {"ips": {self.ipv4}}
        api_url = self.shodan_url + f"/shodan/scan?key={self.shodan_key}"
        r = requests.request(method="POST", url=api_url, params=query, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        id_ = json.loads(r.text)['id']
        api_url = self.shodan_url + f"/shodan/scan/{id_}?key={self.shodan_key}"
        timer = 0
        while(status != 'DONE'):
            r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
            if json.loads(r.text).get('status'):
                sleep(5)
                timer = timer + 5
                status = json.loads(r.text)['status']
                print(status)
                if timer == 60:
                    selector = input("Continue waiting? [y/n]: ")
                    if selector == "n":
                        break
                    else:
                        timer = 0
            else:
                status = 'DONE'
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text

    def shodan_list(self):
        api_url = self.shodan_url + f"/shodan/scans?key={self.shodan_key}"
        r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text
    
    def scan_status(self, id_):
        api_url = self.shodan_url + f"/shodan/scan/{id_}?key={self.shodan_key}"
        r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        if json.loads(r.text).get('status'):
            status = json.loads(r.text)['status']
            if status == 'DONE':
                r_text = self.return_scan(id_)
            else:
                r_text = status
        return r_text
    
    def return_scan(self, id_):
        api_url = self.shodan_url + f"/shodan/host/search?key={self.shodan_key}&query=scan:{id_}"
        r = requests.request(method="GET", url=api_url, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text

