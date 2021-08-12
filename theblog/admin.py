from django.contrib import admin
from .models import BlogPost, Tags, Comments, Profile, Saved
# Register your models here.
admin.site.register(BlogPost),
admin.site.register(Tags),
admin.site.register(Comments),
admin.site.register(Profile),
admin.site.register(Saved),
