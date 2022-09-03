"""URL Config for Shellfish Project"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('librarians/', include('librarians.urls')),
    path('librarians/', include('django.contrib.auth.urls')),
    # path('', RedirectView.as_view(url='catalog/', permanent=True)),
] 

#Config Admin Titles

admin.site.site_header = "Silberberg Library Management System"
admin.site.site_title = "Silberberg Library Management System"
admin.site.index_title = "Admin"