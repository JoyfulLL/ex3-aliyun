from django.conf import settings
from django.conf.urls.static import static
from homeApp89.views import home
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('aboutApp89/', include('aboutApp89.urls')),
    path('contactApp89/', include('contactApp89.urls')),
    path('homeApp89/', include('homeApp89.urls')),
    path('newsApp89/', include('newsApp89.urls')),
    path('productApp89/', include('productApp89.urls')),
    path('scienceApp89/', include('scienceApp89.urls')),
    path('serviceApp89/', include('serviceApp89.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('search/', include('haystack.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
