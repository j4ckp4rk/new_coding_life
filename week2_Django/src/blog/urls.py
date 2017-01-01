from django.conf.urls import url
from . import views
#from 에 .을 찍는 건 같은 폴더내에서 불러온다는 것

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
