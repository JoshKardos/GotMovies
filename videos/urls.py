"""firstDjangoWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import views#look in the samedirectory that you are in add look for file clalled views"""

app_name = "videos"#used in ./videos/urls.py

urlpatterns = [
	#/music/
    url(r'^$',views.IndexView.as_view(),name='index'),#didnt request anything, 'index' is name of function, goes to views file and looks for index

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),#take whatever url, find the function

    #url(r'^results/$',search, name='search'),
   


]
