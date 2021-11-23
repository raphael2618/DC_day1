from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people_view),
    path('people/<int:person_id>/', views.person_view)
]
