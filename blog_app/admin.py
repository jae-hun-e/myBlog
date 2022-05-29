# admin 사이트에서 내가만든객체(ORM)을 확인할 수 있다.
from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)  # admin 사이트에서 Blog객체를 확인할 수 있다.
admin.site.register(Comment)  # admin 사이트에서 Comment객체를 확인할 수 있다.
