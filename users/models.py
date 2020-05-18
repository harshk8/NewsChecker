from django.db import models
from django.contrib.auth.models import User

from news.models import NewsCategory


class UserProfile(models.Model):

	user = models.OneToOneField(
		User,
		related_name='profile',
		on_delete=models.CASCADE
		)
	preferences = models.ManyToManyField(
		NewsCategory,
		related_name='user',
		)
	def __str__(self):
		return self.user