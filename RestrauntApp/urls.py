from django.urls import re_path as url
from RestrauntApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^restraunt$',views.restrauntApi),
    url(r'^restraunt/([0-9]+)$',views.restrauntApi),

    url(r'^menu$', views.menuApi),
    url(r'^menu/([0-9]+)$', views.menuApi)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)