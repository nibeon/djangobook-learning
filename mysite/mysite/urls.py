from django.conf.urls import include, url
from django.contrib import admin

from mysite.views import hello, current_datetime, contact

urlpatterns = [    
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),

    url(r'^contact/$', contact),    
    url(r'^', include('books.urls')),
]
