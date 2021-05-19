from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .logintokenpairview import LoginTokenPairView
admin.autodiscover()
import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("pos/", include("pos.urls")),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api-token-auth/', LoginTokenPairView.as_view(), name='api-tokn-auth'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
