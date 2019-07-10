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
        context['hubs_list'] = self.getHubsData(Hub.FINISHED)
        # context['hubs_list'] = self.updateHubsData()
        return context

    def getHubsData(self, hubStatus):
        self.updateHubsData(hubStatus)

        hubs = Hub.objects.all().filter(status=hubStatus)
        return hubs

    def updateHubsData(self, hubStatus):
        timeThreshold = datetime.utcnow() - timedelta(seconds=10)
        logger.debug("timeThreshold {}".format(timeThreshold))
        """ Update hub data if the one we have is older than x minutes """
        hubs = Hub.objects.all()
        if len(hubs.filter(modified_dttm__lt=timeThreshold)) > 0 or len(hubs.filter(status=Hub.UPCOMING)) == 0:
            hubApiObj = HubApi()
            hubApiObj.collectHubsData()

            for hubNewer in hubApiObj.hubItems:
                try:
                    HubUpdated = Hub.objects.get(faceit_hub_id=hubNewer.getId())
                    HubUpdated.game_id          = hubNewer.getGameId()
                    HubUpdated.name             = hubNewer.getName()
                    HubUpdated.status           = hubNewer.getStatus()
                    HubUpdated.start_dttm       = hubNewer.getStartDttm()
                    HubUpdated.finish_dttm      = hubNewer.getFinishDttm()
                except Hub.DoesNotExist:
                    HubUpdated = Hub(
                        faceit_hub_id   = hubNewer.getId(),
                        game_id         = hubNewer.getGameId(),
                        name            = hubNewer.getName(),
                        status          = hubNewer.getStatus(),
                        start_dttm      = hubNewer.getStartDttm(),
                        finish_dttm     = hubNewer.getFinishDttm()
                    )
                except Hub.ValidationError as err:
                    logger.error("Hub.ValidationError: {}".format(err))
                    continue
                except Hub.FieldError as err:
                    logger.error("Hub.FieldError: {}".format(err))
                    continue

                HubUpdated.save()
        return

class AboutPageView(TemplateView):
    template_name = 'pages/CSGO.html'


	
class LoginPageView(TemplateView):
    # def as_view():

    template_name = '__base.html'









