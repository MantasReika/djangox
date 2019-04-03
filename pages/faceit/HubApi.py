
import logging
from pages.faceit.FaceitApi import FaceitApi
from pages.utils.errlog import VerifyException
# from pages.models import Hub, HubScore, Player, Invites

logger = logging.getLogger(__name__)
logging.basicConfig(filename='applog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class HubData:
    hub_id = ''
    status = ''
    hub_name = ''
    hub_start_dttm = ''
    hub_finish_dttm = ''

    def __init__(self, hub_id='', status='', hub_name='', hub_start_dttm='', hub_finish_dttm=''):
        self.hub_id = hub_id
        self.status = status
        self.hub_name = hub_name
        self.hub_start_dttm = hub_start_dttm
        self.hub_finish_dttm = hub_finish_dttm

class HubApi(FaceitApi):
    hubItems = []

    def __init__(self):
        super().__init__()

    def collectData(self):
        organizerId = 'ca401c56-55fe-40d9-a89e-ac3db2d1395b'
        if organizerId == '':
            organizerId = self.getOrganizer('organizerioName')

        try:
            respHubs = self.getOrganizerHubs(organizerId).json()['items']
            for respHubItem in respHubs:
                respSeason = self.getHubSeason(respHubItem['hub_id'], 1).json()
                HubDataObj = HubData(hub_id=respHubItem['hub_id'])
                HubDataObj.status = respSeason['leaderboard']['status']
                HubDataObj.hub_name = respHubItem['name']
                HubDataObj.hub_start_dttm = respSeason['leaderboard']['start_date']
                HubDataObj.hub_finish_dttm = respSeason['leaderboard']['end_date']

                self.hubItems.append(HubDataObj)

        except VerifyException as err:
            logger.error(err)

    def saveResponse(self):
        pass
        # for respHub in self.respHubs:
        #     try:
        #         self.updateHub(respHub)
        #     except Hub.DoesNotExist:
        #         self.createHub(respHub)

    def createHub(self):
        pass
        # hubObj = Hub(
        #     status=self.parseStatus(respHub['']),
        #     hub_name=
        # )
