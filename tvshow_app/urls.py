from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.create),
    path('shows/<int:show_id>', views.display),
    path('shows/<int:show_id>/edit', views.update),
    path('shows/<int:show_id>/destroy', views.destroy),
]
