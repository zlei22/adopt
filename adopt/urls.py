from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.all_pets),
    path('add/', views.add_pet),
    path('<int:pet_id>', views.pet_details),
    path('<int:pet_id>/edit/', views.edit_pet),
]
