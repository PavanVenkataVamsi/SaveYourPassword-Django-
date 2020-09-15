from django.db import models

# Create your models here.
class DataBase(models.Model):
	username=models.CharField(max_length=30,unique=True)
	Email=models.EmailField()
	password=models.CharField(max_length=50)
	gitu=models.CharField(max_length=30,blank=True)
	gitpas=models.CharField(max_length=50,blank=True)
	faceu=models.CharField(max_length=30,blank=True)
	facepas=models.CharField(max_length=50,blank=True)
	instau=models.CharField(max_length=30,blank=True)
	instapas=models.CharField(max_length=50,blank=True)
	stau=models.CharField(max_length=30,blank=True)
	stapas=models.CharField(max_length=50,blank=True)