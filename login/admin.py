from django.contrib import admin
from .models import Home, Register
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ("nama", "keterangan",)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ("nama",)

admin.site.register(Home, HomeAdmin)
admin.site.register(Register, RegisterAdmin)