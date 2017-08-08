# -*- coding: utf-8 -*-
import os, datetime, uuid, rules
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from .predicates import *



class Module(models.Model):

	key = models.UUIDField(primary_key=True, max_length=32, default=uuid.uuid4, editable=False, verbose_name="clé")
	name = models.CharField(max_length=255)
	fields = models.CharField(max_length=5000, null=True, blank=True)

	def __str__(self): return self.name
	def get_absolute_url(self): return reverse('sites__module_detail', kwargs={'pk': self.key,})


class Site(models.Model):

	key = models.UUIDField(primary_key=True, max_length=32, default=uuid.uuid4, editable=False, verbose_name="clé")
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, related_name='sites_created')

	name = models.CharField(max_length=60, verbose_name="titre")
	description = models.CharField(max_length=160)
	modules = models.ManyToManyField(Module, through="SiteModule", blank=True)
	editors = models.ManyToManyField(User, related_name='sites_that_can_be_edited')

#	theme = ***
#	published = ***

	def __str__(self): return '{} ({})'.format(self.name, str(self.key)[:8])
	def get_absolute_url(self): return reverse('sites__site_update', kwargs={'pk': self.key,})

rules.add_rule('can_update_site', is_site_editor | is_superuser)


# class SiteEdit(models.Model):
	# tracks editing history of sites



class SiteModule(models.Model):

	site = models.ForeignKey(Site)
	module = models.ForeignKey(Module)
	data = models.CharField(max_length=5000, null=True, blank=True)
	order = models.IntegerField()

	class Meta :
		ordering = ['order',]