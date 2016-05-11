from django.conf.urls import url
#test
from . import views

app_name = "shop"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

