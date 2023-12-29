from django.db import models

# Create your models here.
   
class Home(models.Model):
    nama = models.CharField(max_length=225)
    keterangan = models.TextField()
    harga = models.TextField()

    def __str__(self):
        return f"{self.nama}"

class Blogs(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    informasi = models.CharField(max_length=225)
    keterangan = models.TextField()    

    def __str__(self):
        return f"{self.informasi}"


class Portofolio(models.Model):
    project = models.CharField(max_length=225)
    keterangan = models.TextField()    

    def __str__(self):
        return f"{self.project}"