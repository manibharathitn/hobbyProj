from django.conf.urls.defaults import patterns, include, url
from dashboard import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$',views.detail),
	url(r'^plotgraph_pendingbooking',views.getPendingBooking),
)
