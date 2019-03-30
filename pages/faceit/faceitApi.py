import requests
class faceitApi:
    def __init__(self, apiToken='930a729e-c82b-427b-a35b-4a8101ec31ff'):
        self.apiToken = apiToken
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(apiToken)}
        self.apiUrlBase = 'https://open.faceit.com/data/v4'

    def makeUrl(self, apiUrlBase, apiResource):
        return '{0}{1}'.format(apiUrlBase, apiResource)

    def callApi(self):
        return requests.get(self.apiUrl, headers=self.headers, params=self.params)

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