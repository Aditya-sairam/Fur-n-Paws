from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='media/image/default',upload_to='media/image/')

	def __str__(self):
		return f'{self.user.username} profile'