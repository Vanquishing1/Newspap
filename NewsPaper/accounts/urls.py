from django.urls import path
from .views import edit_profile
from .views import become_author

urlpatterns = [
    path('edit/', edit_profile, name='edit_profile'),
    path('become_author/', become_author, name='become_author'),
]
