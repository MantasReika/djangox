import logging
from pages.utils.errlog import VerifyException

logger = logging.getLogger(__name__)
logging.basicConfig(filename='applog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(threadName)s %(levelname)s: %(message)s')

import requests
class FaceitApi:
    def __init__(self, apiToken='930a729e-c82b-427b-a35b-4a8101ec31ff'):
        self.apiToken = apiToken
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(apiToken)}
        self.apiUrlBase = 'https://open.faceit.com/data/v4'

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def collectHubsData(self):
        raise Exception("Method must be implemented in child class")

    def saveResponse(self):
        raise Exception("Method must be implemented in child class")

    def makeUrl(self, apiUrlBase, apiResource):
        return '{0}{1}'.format(apiUrlBase, apiResource)

    def callApi(self):
        resp = requests.get(self.apiUrl, headers=self.headers, params=self.params)
        self.verifyResponse(resp, self.apiUrl, self.params)
        return resp

    def getOrganizer(self, name):
        self.apiResource = '/organizers'
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {'name' : name}
        return self.callApi()

    def getOrganizerTournaments(self, organizerId):
        self.apiResource = '/organizers/{0}/tournaments'.format(organizerId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getTournaments(self):
        self.apiResource = '/tournaments'
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getTournament(self, tournamentId):
        self.apiResource = '/tournaments/{0}'.format(tournamentId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getTournamentMatches(self, tournamentId):
        self.apiResource = '/tournaments/{0}/matches'.format(tournamentId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getTeam(self, teamId):
        self.apiResource = '/teams/{0}'.format(teamId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getPlayer(self, playerName):
        self.apiResource = '/search/players'
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {'nickname' : playerName}
        return self.callApi()

    def getOrganizerHubs(self, organizerId):
        self.apiResource = '/organizers/{0}/hubs'.format(organizerId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getHub(self, hubId):
        self.apiResource = '/hubs/{0}'.format(hubId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def getHubSeason(self, hubId, seasonId):
        self.apiResource = '/leaderboards/hubs/{0}/seasons/{1}'.format(hubId, seasonId)
        self.apiUrl = self.makeUrl(self.apiUrlBase, self.apiResource)
        self.params = {}
        return self.callApi()

    def verifyResponse(self, resp, url, param):
        try:
            errorMsg = resp.json()['errors'][0]
            hasErr = True

        except KeyError:
            hasErr = False

        if hasErr:
            raise VerifyException("verifyResponse:[ err_msg:{0}; url:{1}; param:{2}]".format(errorMsg["message"],url, param))

        """
    {
        "errors": [
            {
                "message": "There was something wrong with your request.",
                "code": "err_br0",
                "http_status": 400,
                "parameters": []
            }
        ]
    }
            """