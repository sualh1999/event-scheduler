from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('start_time')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
