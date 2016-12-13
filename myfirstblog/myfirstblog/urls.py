"""myfirstblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myfirstblog.views import linyuelin,hello,my_homepage_view,current_datetime
from blog.views import shanhtml


urlpatterns = [
    url(r'^linyuelin/', linyuelin),
    url(r'^homepage/', my_homepage_view),
    url(r'^shanhtml/', shanhtml),
    url(r'^admin/', admin.site.urls),

]
