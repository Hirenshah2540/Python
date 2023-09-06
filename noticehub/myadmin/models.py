from django.db import models

class Register(models.Model):
	name  = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	contact=models.BigIntegerField()
	created_at = models.DateTimeField(auto_now=True)


	class Meta:
		db_table = 'register'

class Notice(models.Model):
	subject = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'notice'

