from django.contrib import admin
from .models.users import User
from .models.post import Post

admin.site.register(User)
admin.site.register(Post)
