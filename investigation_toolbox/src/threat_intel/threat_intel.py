import requests
import docs.conf as conf
import json

class intel_queries():
    def __init__(self, intel):
        self.intel = intel
        self.threat_miner_key = conf.api_conf['api']['threat_miner']['key']
        self.threat_miner_url = conf.api_conf['api']['threat_miner']['url']

    def threat_miner(self):
        querystring = {
            "key": self.threat_miner_key,
            "format": "json"
        }
        r = requests.request(method="GET", url=self.threat_miner_url, params=querystring, timeout=conf.request_timeout)
        r_text = json.dumps(r.json(), sort_keys=False, indent=4)
        return r_text
