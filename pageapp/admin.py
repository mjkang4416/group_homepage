from django.contrib import admin
# Register your models here.
from pageapp.models import passList
from pageapp.models import userList

admin.site.register(passList)
admin.site.register(userList)
