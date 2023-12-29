from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from .models import Home, Blogs, Portofolio
from django.contrib import messages

def login(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def home(request):
  data = Home.objects.all()
  template = loader.get_template('home.html')
  context = {
    'jasa': 'Daftar Tabel Jasa Yang Tersedia',
    'home': data
  }
  return HttpResponse(template.render(context, request))

def blogs(request):
  data_home = Home.objects.all()
  data = Blogs.objects.all()
  template = loader.get_template('blogs.html')
  context = {
    'jual': 'Daftar Informasi Penjualan Jasa DF Services',
    'home': data_home,
    'blogs': data
  }
  return HttpResponse(template.render(context, request))

def blogsjasa(request, id):
  data = Blogs.objects.filter(id=id).first()
  template = loader.get_template('blogsjasa.html')
  context = {
    'blogs': data
  }
  return HttpResponse(template.render(context))

def portofolio(request):
  datap = Portofolio.objects.filter(project='Website Data Siswa/i SMKN3 PAMEKASAN').values()
  datak = Portofolio.objects.filter(project='Website Perpustakaan SMKN3 PAMEKASAN').values()
  datakt = Portofolio.objects.filter(project='Website Toko Onilne RumahBatikMJ').values()
  datakp = Portofolio.objects.filter(project='Website Toko Online Jasa DF Services').values()
  datakl = Portofolio.objects.filter(project='Website My Portofolio | Defilia Fatikasari').values()
  template = loader.get_template('portofolio.html')
  context = {
    'port1': datap,
    'port2': datak,
    'port3': datakt,
    'port4': datakp,
    'port5': datakl
  }
  return HttpResponse(template.render(context, request))

def add_item(request):
  if request.method=="POST":
    home_id = request.POST['home']
    informasi = request.POST['informasi']
    keterangan = request.POST['keterangan']
    home_instance = Home.objects.get(id=home_id)

    blogs = Blogs(home=home_instance, informasi=informasi, keterangan=keterangan)
    blogs.save()
    messages.info(request, "DATA BERHASIL DITAMBAHKAN")
    return redirect('blogs')
  else:
    pass

  blogs_list = Blogs.objects.all()
  context = {
    'blogs_list': blogs_list
  }
  template = loader.get_template('blogs.html')
  return HttpResponse(template.render(context, request))

def delete_item(request, id):
  blogs = Blogs.objects.get(id = id)
  blogs.delete()
  messages.info(request, "DATA BERHASIL DI HAPUS")
  return redirect('blogs')

def update_item(request, id):
  sel_blogs = Blogs.objects.get(id = id)
  data_home = Home.objects.all()
  blogs = Blogs.objects.all()
  context = {
    'jual': 'Edit Daftar Informasi Penjualan Jasa DF Services',
    'sel_blogs': sel_blogs,
    'home': data_home,
    'blogs': blogs
  }
  template = loader.get_template('blogs.html')
  return HttpResponse(template.render(context, request))

def edit_item(request, id):
  blogs = Blogs.objects.get(id = id)
  blogs.home_id = request.POST['home']
  blogs.informasi = request.POST['informasi']
  blogs.keterangan = request.POST['keterangan']
  blogs.save()
  messages.info(request, "DATA BERHASIL DI EDIT")
  return redirect('blogs')