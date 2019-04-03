from django.views.generic import TemplateView

from pages.faceit.FaceitApi import FaceitApi

from .models import Hub, HubScore, Player, Invites
import json

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['tournaments_list'] = self.getTournaments()
        context['tournaments_list'] = self.updateTournaments()
        return context

    def getTournaments(self):
        try:
            tournaments = Hub.objects.get(sta=Hub.UPCOMING)
        except:
            return []
        return tournaments

    def updateTournaments(self):
        organizerId = 'ca401c56-55fe-40d9-a89e-ac3db2d1395b'  # organizerData['organizer_id']

        api = faceitApi()
        apiTournaments = api.getOrganizerHubs(organizerId)
        return apiTournaments.json()['items']

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
	
class IndexPageView(TemplateView):
    # def as_view():

    template_name = 'pages/index.html'

class LoginPageView(TemplateView):
    # def as_view():

    template_name = '__base.html'
