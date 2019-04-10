from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('<str:import_country>/', views.details, name='detail'),
]

urlpatterns += staticfiles_urlpatterns()