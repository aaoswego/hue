from __future__ import unicode_literals

from django.db import models

class LightButton(models.Model):
	button_text = models.CharField(max_length=50)
	button_url = models.CharField(max_length=500)
