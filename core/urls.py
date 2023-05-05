from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    
    # accounts urls
    path("accounts/", include([
        path("", include("accounts.urls")),
        path("", include("registration.backends.default.urls")),
    ])),
    
    # app urls
    path("", include("app.urls")),
]
# statics urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handlers configuration
handler400 = 'core.handlers.handler400'
handler403 = 'core.handlers.handler403'
handler404 = 'core.handlers.handler404'
handler500 = 'core.handlers.handler500'

# debug toolbar urls
if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')),)