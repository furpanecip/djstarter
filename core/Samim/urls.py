from django.contrib import admin
from django.urls import include, path

from .views import landing

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", landing, name="konak"),
    path("dashboard/", include("tatbikat.idare.urls")),
    path('accounts/', include('allauth.urls')),
]
