from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Infinity API ",
        default_version="v1",
        description="Ecommerce project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="prodeveloper502@gmail.com"),
        license=openapi.License(name="demo license"),
    ),
    public=True,
    permission_classes=[
        AllowAny,
    ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("users.url")),
    path("post/", include("posts.url")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)