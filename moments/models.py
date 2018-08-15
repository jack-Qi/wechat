from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WeChatUser(models.Model):
	user = models.OneToOneField(User)
	motto = models.CharField(max_length=500, null=True, blank=True)
	pic = models.CharField(max_length=200, null= True, blank= True)
	region = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username

	class Meta:
		ordering = ['id']

class Status(models.Model):
	user = models.ForeignKey(WeChatUser)
	text = models.CharField(max_length=140)
	pics = models.CharField(max_length=400, null=True, blank=True)
	pub_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

	def __str__(self):
		return self.text

	class Meta:
		ordering = ['-id']