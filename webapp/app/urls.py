from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("filter-ionograms/<int:id>", views.filter_ionograms, name='filter'),
    path("edit-transmitter/<int:id>", views.edit_transmitter, name='edit-transmitter'),
    path("receiver-info", views.receiver_info, name='receiver-info'),
    path("filter_ionograms", views.filter_ionogramss, name='filter_ionograms'),
]
