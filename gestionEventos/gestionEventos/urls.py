from django.urls import path
from evento.views import EventoListCreate, EventoRetrieveUpdateDestroy

urlpatterns = [
    path('eventos/', EventoListCreate.as_view()),
    path('eventos/<int:pk>/', EventoRetrieveUpdateDestroy.as_view()),
]