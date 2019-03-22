from django.contrib import admin

# Register your models here.
from .models import post
from .models import Like,Comment
# Register your models here.
admin.site.register(post)
admin.site.register(Like)
admin.site.register(Comment)