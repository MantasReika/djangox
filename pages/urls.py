from django.urls import path

from django.conf.urls import url

from .views import AboutPageView, IndexPageView, LoginPageView

from . import views


urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('CSGO_tips', AboutPageView.as_view(), name='tips'),
    path('test/login', LoginPageView.as_view(), name='login'),

]
