from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic


admin.autodiscover()


urlpatterns = patterns("",

    # Admin URLs.
    url(r"^admin/", include(admin.site.urls)),
    
    # There's no favicon here!
    url(r"^favicon.ico$", generic.RedirectView.as_view()),
    url(r'^$', 'website.views.home', name='home'),
    url(r'^about$', 'website.views.about', name='about'),
    url(r'^photos$', 'website.views.photos', name='photos'),
    url(r'^pricing$', 'website.views.pricing', name='pricing'),
    url(r'^contact$', 'website.views.contact', name='contact'),
    url(r'^reserve$', 'website.views.about', name='reserve'),
    url(r'^index$', 'website.views.home', name='index'),    
)
