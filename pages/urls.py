from django.urls import path

from .views import AboutPageView, IndexPageView, LoginPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('test/login', LoginPageView.as_view(), name='login'),
]
