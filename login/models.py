from django.db import models

# Create your models here.
class Home(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField()

    def __str__(self):
        return f"{self.nama}"
    
class Register(models.Model):
    nama = models.CharField(max_length=100)    

    def __str__(self):
        return f"{self.nama}"