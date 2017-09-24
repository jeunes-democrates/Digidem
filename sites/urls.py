from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views

UUID_PK = r'(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})' # UUID

urlpatterns = [
#	url(r'^$', views.Dashboard, name='sites__dashboard'),
	url(r'^$', views.Dashboard.as_view(), name='sites__dashboard'),
	url(r'^site/{}/'.format(UUID_PK), views.SiteUpdate.as_view(), name='sites__site_update'),
	url(r'^site/créer/'.format(UUID_PK), views.SiteCreate.as_view(), name='sites__site_create'),
	url(r'^modèle-de-module/{}/'.format(UUID_PK), views.ModuleTemplateDetail.as_view(), name='sites__module_template_detail'),
]