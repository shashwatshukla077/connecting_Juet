from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class juetpost(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	def __str__(self):
		return self.title
# Create your models here.
