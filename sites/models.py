# -*- coding: utf-8 -*-
import os, datetime, uuid, json, rules
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from .predicates import *



class ModuleTemplate(models.Model):

	slug = models.SlugField(primary_key=True, max_length=64, allow_unicode=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	fields = models.CharField(max_length=5000, null=True, blank=True)

	def __str__(self): return self.slug
	def get_absolute_url(self): return reverse('sites__module_template_detail', kwargs={'slug': self.slug,})
	def get_fields(self): return json.loads(self.fields)



class Site(models.Model):

	key = models.UUIDField(primary_key=True, max_length=32, default=uuid.uuid4, editable=False, verbose_name="clé")
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, related_name='sites_created', null=True, on_delete=models.SET_NULL )

	name = models.CharField(
		verbose_name="titre",
		max_length=60,
		default="Jeunes Démocrates de ...",
		help_text="Max. 60 | Idéalement au format \"Jeunes Démocrates de Corse\"."
		)

	description = models.CharField(
		max_length=160, 
		help_text="Max. 160 | Ex. \"Groupe local représentant les jeunes miltants du Mouvement Démocrate\"", default="Groupe local représentant les jeunes miltants du Mouvement Démocrate"
		)

	editors = models.ManyToManyField(User, related_name='sites_that_can_be_edited')

#	theme = ***
#	published = ***

	def __str__(self): return '{} ({})'.format(self.name, str(self.key)[:8])
	def get_absolute_url(self): return reverse('sites__site_update', kwargs={'pk': self.key,})

rules.add_rule('can_update_site', is_site_editor | is_superuser)



class Module(models.Model):

	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	template = models.ForeignKey(ModuleTemplate, on_delete=models.CASCADE)
	data = models.CharField(max_length=100000, null=True, blank=True)
	order = models.IntegerField(null=True, blank=True)

	def __str__(self):
 		#if self.get_title() :
 		#	return "{} ({})".format(self.get_title(), self.template)
 		#else : 
		return str(self.template)

	def get_values(self):
		if self.data :
			return json.loads(self.data)
		else :
			return dict()

	def get_title(self):
		values = self.get_values()
		try :
			return values['title']
		except Exception:
			return self.template.slug

	def get_text(self):
		values = self.get_values()
		try :
			return markdownify(values['text'])
		except Exception:
			return ""


	class Meta :
		ordering = ['order',]