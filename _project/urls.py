from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

admin.site.site_header = 'Digidem - Administration'

urlpatterns = [
	url('^', include('django.contrib.auth.urls')), # keeping this for the logout feature
	url('^', include('sites.urls')),
	url(r'^auth/', include('django_auth_network_client.urls')),
	url(r'^arriere-boutique/login/', RedirectView.as_view(url="/auth", permanent=False)), # override native admin auth
	url(r'^arriere-boutique/', admin.site.urls, name='admin'),
]