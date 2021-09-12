from rest_framework import generics
from .serializers import LogSerializer
from .models import Log
from .permissions import IsOwnerOrReadOnly

class LogList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class LogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Log.objects.all()
    serializer_class = LogSerializer
