from django.db import models

class Name(models.Model):
	name = models.CharField(max_length=200,null=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
