"""
URL configuration for back_package_managment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from packages.views import ListPackage, GetPackage
from items.views import GetItemsFromPackage

schema_view = get_schema_view(
    openapi.Info(
        title="Technical Test API",
        default_version="v1",
        description="API Rest for Technical Test",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api-auth/", include("rest_framework.urls")),
    path("list-package/", ListPackage.as_view(), name="list-package"),
    path(
        "package/<package_code>/", GetPackage.as_view(), name="retrieve-package-infos"
    ),
    path(
        "items/<package_code>/",
        GetItemsFromPackage.as_view(),
        name="retrieve-items-infos",
    ),
]
