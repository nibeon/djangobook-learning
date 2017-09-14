# from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

# from mysite.views import hello, current_datetime, hours_ahead, contact

from . import views

urlpatterns = [    
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^contact/$', views.contact),    
    url(r'^', include('books.urls')),
]

# if settings.DEBUG:
#    urlpatterns += [url(r'^debuginfo/$', views.debug),]