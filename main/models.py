from django.db import models

class SomeModel(models.Model):
	somefield = models.CharField(max_length=255)

	def to_lowercase(self):
		return self.somefield.lower()
