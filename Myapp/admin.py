from django.contrib import admin

# Register your models here.
from Myapp.models import *

admin.site.register(DB_News)
admin.site.register(DB_projects)
admin.site.register(DB_new_srs)