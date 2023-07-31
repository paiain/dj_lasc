
from django.contrib import admin
from webpage.models import LOGIN, crtateuser ,activity,Profile,add_ativity,add_data,add_data_all

# Register your models here.

admin.site.register(crtateuser)
admin.site.register(LOGIN)
admin.site.register(activity)
admin.site.register(Profile)
admin.site.register(add_ativity)
admin.site.register(add_data)
admin.site.register(add_data_all)

