from django.db import models

# Create your models here.
class NewsModel(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to='media/')
	date = models.DateField()

class TeachersModel(models.Model):
	full_name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='media/programmers/')
	

class ProgramsModel(models.Model):
	title = models.CharField(max_length=255)
	credits = models.IntegerField(default=0)
	time = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='media/teachers/')
	date = models.DateField()


class AboutUniversityModel(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()