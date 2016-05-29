from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('app.urls')),
	url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/',}),
]
