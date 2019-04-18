"""template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.contrib import admin
# 可能需要的访问static配置
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import *
from user import views
from django.views.static import serve
# 图片上传路径
from project.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', views.toLoginView),
    # path('admin/', admin.site.urls),
    path('user/', include('user.urls')),

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
