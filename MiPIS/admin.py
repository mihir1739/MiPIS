from django.contrib import admin
from MiPIS.models import User,Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User)
admin.site.register(Data,DataAdmin)