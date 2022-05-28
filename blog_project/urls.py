from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    # html form을 이용해서 blog 객체 만들기
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),

    # Django form을 이용한 Blog 객체 만들기
    path('formcreate/', views.form_create, name="form_create"),

    # model form을 이용한 blog 객체 만들기
    path('modelformcreate', views.modelformcreate, name='modelformcreate'),
]
