from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer

class EventoListCreate(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer