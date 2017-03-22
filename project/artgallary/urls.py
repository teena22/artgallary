"""artgallary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include
from myart.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'), 
    url(r'^logout/', logout_view, name='logout'), 
    url(r'',include('myart.urls')), 
] 

'''if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns = [
       url (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})]'''

#from django.conf import settings
#from django.conf.urls.static import static
