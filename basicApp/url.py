from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path(r'download/<int:id>/', views.downLoadFile),
    # path(r'^download/(?P<user_id>\d+)/$', views.downLoadFile),
    path("upload", views.uploadFile),
]