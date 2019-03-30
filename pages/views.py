from django.views.generic import TemplateView

from pages.faceit.faceitApi import faceitApi
import json

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tournaments_list'] = self.getTournaments()
        return context

    def getTournaments(self):
        organizerId = 'ca401c56-55fe-40d9-a89e-ac3db2d1395b'  # organizerData['organizer_id']

        api = faceitApi()
        tournaments = api.getOrganizerHubs(organizerId)
        return tournaments.json()['items']


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
	
class IndexPageView(TemplateView):
    # def as_view():

    template_name = 'pages/index.html'

class LoginPageView(TemplateView):
    # def as_view():

    template_name = '__base.html'
