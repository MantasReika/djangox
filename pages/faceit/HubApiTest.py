from pages.faceit.HubApi import HubData, HubApi
import json

def printJson(data):
    print(json.dumps(data, indent=2, sort_keys=True))


hub = HubApi()
hub.collectHubsData()
for i in hub.hubItems:
    print(i)
    printJson(i.__dict__)

# print(hub.hubItems)