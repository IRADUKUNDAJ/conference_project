from django.contrib import admin

# Register your models here.
from .models import conference #new
 #new
admin.site.register(conference)
