from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from shop.views import ProductViewSet

router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # maintenance mode for production
    url(r'^soon', include('comingsoon.urls', namespace='comingsoon')),
#    url(r'^api/', include(router.urls)),
#    url(r'^cart/', include('cart.urls', namespace='cart')),
#    url(r'^payment/', include('payment.urls', namespace='payment')),
#    url(r'^orders/', include('orders.urls', namespace='orders')),
#    url(r'^paypal/', include('paypal.standard.ipn.urls')),
#    url(r'^', include('shop.urls', namespace='shop')),

    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
