from django.db import models

class cateogies(models.Model):
	name = models.CharField(max_length=80,null=False)
	thumbnail = models.ImageField(upload_to='photos')
	description = models.TextField(max_length=300)
	upload_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(null=False)

	def __str__(self):
		return self.name