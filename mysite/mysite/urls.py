from django.conf.urls import include, url
from django.contrib import admin

from mysite.views import hello, contact

urlpatterns = [
    url(r'^', include('books.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^contact/$', contact),
    # url(r'^time/$', current_datetime),
]
