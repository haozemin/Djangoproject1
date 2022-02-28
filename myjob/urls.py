from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #2.新增应用的路由配置信息
    path('',views.get_index_page)
]