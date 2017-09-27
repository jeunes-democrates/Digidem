import random, ast
from datetime import datetime, timedelta
from django.db.models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from .models import *



class ModuleTemplateDetail(LoginRequiredMixin, DetailView):
	model = ModuleTemplate
	template_name = 'sites/module-template.html'


class Dashboard(LoginRequiredMixin, TemplateView):
	template_name = 'sites/overview.html'


class SiteCreate(LoginRequiredMixin, CreateView):

	model = Site
	fields = ['name', 'description', ]
	template_name = 'form.html'

	def form_valid(self, form):
		site = form.save(commit=False)
		# Add the user as creator
		site.created_by = self.request.user
		site.save()
		site.editors.add(self.request.user)
		return super(SiteCreate, self).form_valid(form)

	def title(self):
		return "Créer un site"


def AddBasicModulesToSite(site):
	template = ModuleTemplate.objects.all()[0]
	Module.objects.create(site=site, template=template, data='{"potato": 1}', order=1)
	Module.objects.create(site=site, template=template, data='{"potato": 1}', order=2)
	Module.objects.create(site=site, template=template, data='{"potato": 1}', order=3)
	#Todo : create 3 modules
	# add teh modules via fixtures



class SitePreview(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

	model = Site
	permission_required = 'site.update_site'
	fields = ['name', 'description', ]
	template_name = 'sites/preview/base.html'

'''
class SitePreview(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

	model = Site
	permission_required = 'site.update_site'
	fields = ['name', 'description', ]
	template_name = 'sites/preview/base.html'
'''

class SiteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

	model = Site
	permission_required = 'site.update_site'
	fields = ['name', 'description', ]
	template_name = 'sites/site.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		SiteModule.objects.filter(site = self.object).delete()
		for module in form.cleaned_data['modules']:
			# Create SiteModules to fits
			site_module = SiteModule(site = self.object, module = module,)
			site_module.save()
		return super(SiteUpdate, self).form_valid(form)


