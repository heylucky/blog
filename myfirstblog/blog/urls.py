from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shanhtml/$', views.shanhtml, name='shanhtml'),
]