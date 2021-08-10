from django.urls import path

from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gallery_view, name='gallery-home'),
    # path('test/', views.test_view, name='test-view'),
    path('test/flare.csv', RedirectView.as_view(url=staticfiles_storage.url('flare.csv')))
]
