"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from eshop import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.staticfiles.urls import *
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from solid_i18n.urls import solid_i18n_patterns
from django.utils.translation import ugettext_lazy as _

"""
urlpatterns = solid_i18n_patterns('',
   url(r'^about/$', views.about, name='about'),
        url(r'^work/$', views.portfolio_list, name='portfolio_list'),
        url(r'^faq/$', views.faq, name='faq'),
        url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
        url(r'^categories/$', views.category_list, name='category_list'),
        url(r'^categories/(?P<category_slug>[-\w]+)/$', views.productlist_by_category, name='productlist_by_category'),
        url(r'^product/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^page/(?P<pk>[0-9]+)/$', views.page_detail, name='page_detail'),

)"""

# without i18n
urlpatterns += patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^i18n/', include('django.conf.urls.i18n')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


##code bellow added to fix server error when debug mode disabled
## this solution includes that portfolio/urls.py is not used anymore

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),
    )

# add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]


#add rosetta urls
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
