from django.db import models
from cart.models import Cart 



STATUS_CHOICES = (("Started","Started"),("Abandoned","Abandoned"),("Finished","Finshed"))


class Order(models.Model):
	cart = Cart.ForeignKey(Cart)
	status = models.CharField(max_length=120,choices = STATUS_CHOICES,default="Started")

