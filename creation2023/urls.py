"""
URL configuration for creation2023 project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from club.sitemaps import PostSitemap

admin.site.site_header = 'CreationClub Admin'
admin.site.site_title = 'CreationClub@admin'
admin.site.site_url = ''
admin.site.index_title = 'CreationClub administration'
admin.empty_value_display = '**Empty**'

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("dashboard/", admin.site.urls),
    path("", include("club.urls"), name="blog-urls"),
    path("summernote/", include("django_summernote.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("backgroud-removal/", include("techno.urls"), name="techno-urls"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)