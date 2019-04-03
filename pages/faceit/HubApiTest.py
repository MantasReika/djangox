from pages.faceit.HubApi import HubData, HubApi
import json

def printJson(data):
    print(json.dumps(data, indent=2, sort_keys=True))


hub = HubApi()
hub.collectData()
print(hub.hubItems)