from django.contrib import admin
from .models import Post 
# Register your models here.

# The below line register our model so that we can view at our admin page.
admin.site.register(Post)
