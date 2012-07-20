from django.db import models

# Create your models here.

class Etudiant(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=100)
	email = models.EmailField()

class Copie(models.Model):
	num = models.IntegerField()
	image_nom = models.ImageField(upload_to="images")	

class Associate(models.Model):
	copie = models.ForeignKey(Copie)
	etudiant = models.ForeignKey(Etudiant)
