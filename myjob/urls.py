from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),不能重复定义会出现错误：?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
    #2.新增应用的路由配置信息
    path('',views.get_index_page)
]