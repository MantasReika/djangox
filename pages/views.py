from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tournaments_list'] = self.getTournaments()
        return context

    def getTournaments(self):

        tournaments = [
            {'trName' : 'test tournament1',
             'trTime' : '10:00:00'
             },
            {'trName': 'test tournament2',
             'trTime': '12:00:00'
             },
            {'trName': 'test tournament3',
             'trTime': '13:00:00'
             }
        ]
        return tournaments


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
	
class IndexPageView(TemplateView):
    # def as_view():

    template_name = 'pages/index.html'

class LoginPageView(TemplateView):
    # def as_view():

    template_name = '__base.html'
