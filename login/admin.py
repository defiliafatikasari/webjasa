from django.contrib import admin
from .models import Home, Blogs, Portofolio
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan", "harga",)

class BlogsAdmin(admin.ModelAdmin):
    list_display = ("informasi", "keterangan",)

class PortofolioAdmin(admin.ModelAdmin):
    list_display = ("project", "keterangan",)

admin.site.register(Home, HomeAdmin)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Portofolio, PortofolioAdmin)