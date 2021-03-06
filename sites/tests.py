from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from .models import *

import rules



class ModuleTemplateTestCase(TestCase):


	def setUp(self):

		self.module_template = ModuleTemplate.objects.create(
			name="Texte libre",
			fields='''
				[
					{
						"name": "Titre",
						"type": "text_short",
						"default": "À propos"
					},
					{
						"name": "Texte",
						"type": "text_markdown",
						"default": "Notre objectif est la défense et le développement des valeurs démocrates sur le territoire Westerosi. Les libertés individuelles et économiques, la responsabilité de chaque individu, la justice sociale, l'Europe et l'environnement sont au coeur de notre engagement.",
						"help_text": "Utilisez la syntaxe <a href='https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet' target='_blank'>Markdown</a>, par exemple pour écrire en <strong>**gras**</strong> ou en <em>__italique__</em>, ou encore pour insérer des liens, des images ou des titres."
					}
				]'''
			)