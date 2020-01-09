"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


'''
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'mydemo/', include('mydemo.urls'))
]
'''

from django.contrib import admin
from django.urls import path
from mydemo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gdp_year)  # 添加路径对应函数，''表示运行首页访问路径
    #path('', views.gdp_growth)  # 添加路径对应函数，''表示运行首页访问路径
]
