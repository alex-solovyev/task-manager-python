from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tag, Task, User

admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(User, UserAdmin)
