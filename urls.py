# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url
from extend.views import *
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    (r'^picture/(?P<path>.*)','django.views.static.serve',{'document_root':'./extend/'}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', show_homepage),
    url(r'^add$',add_book),
    url(r'^add_author/',add_author),
    url(r'^search/',search_book),
    url(r'^information/',information),
    url(r'^delete/',delete_book),
    url(r'^updata/',updata_book),
    url(r'^delete_author/',delete_author)
    )
