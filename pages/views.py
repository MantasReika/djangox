import logging

from django.views.generic import TemplateView
from pages.faceit.HubApi import HubApi
from .models import Hub, HubScore, Player, Invites

from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)
logging.basicConfig(filename='applog.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class IndexPageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hubs_list'] = self.getHubsData()
        # context['hubs_list'] = self.updateHubsData()
        return context

    def getHubsData(self):
        self.updateHubsData()

        hubs = Hub.objects.all().filter(status=Hub.UPCOMING)
        return hubs
        # try:
        #     competitions = Hub.objects.get(sta=Hub.UPCOMING)
        # except:
        #     return []
        # return competitions

    def updateHubsData(self):
        timeThreshold = datetime.now() - timedelta(minutes=1)
        """ Update hub data if the one we have is older than x minutes """
        hubs = Hub.objects.all()
        logger.debug('Got hubs from db, len: {}'.format(len(hubs)))
        if len(hubs.filter(modified_dttm__lt=timeThreshold)) > 0 or len(hubs.filter(status=Hub.UPCOMING)) == 0:
            hubApiObj = HubApi()
            hubApiObj.collectHubsData()
            logger.debug('Got hubs from API')
            for hubNewer in hubApiObj.hubItems:
                # for hub in hubs.objects.filter():
                #     if hubNewer.id == hub.faceit_hub_id:
                logger.debug('Processing for {}'.format(hubNewer.id))
                try:
                    HubUpdated = Hub.objects.get(faceit_hub_id=hubNewer.id)
                    HubUpdated.game_id          = hubNewer.game_id
                    HubUpdated.name             = hubNewer.name
                    # HubUpdated.status           = hubNewer.status
                    # HubUpdated.start_dttm       = hubNewer.start_dttm
                    # HubUpdated.finish_dttm      = hubNewer.finish_dttm
                    logger.debug('Updated hub {}'.format(hubNewer.id))
                    logger.debug(hubNewer.__dict__  )
                except Hub.DoesNotExist:
                    HubUpdated = Hub(
                        faceit_hub_id   = hubNewer.id,
                        game_id         = hubNewer.game_id,
                        name            = hubNewer.name,
                        # status          = hubNewer.status,
                        # start_dttm      = hubNewer.start_dttm,
                        # finish_dttm     = hubNewer.finish_dttm
                        )
                    logger.debug('Created hub {}'.format(hubNewer.id))

                HubUpdated.save()
        return

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
	
class LoginPageView(TemplateView):
    # def as_view():

    template_name = '__base.html'
