from rest_framework import viewsets
from .permissions import IsOwner
from . import models
from . import serializers


class FriendViewset(viewsets.ModelViewSet):
     queryset = models.Friend.objects.all()
     serializer_class = serializers.FriendSerializer
     permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
     queryset = models.Belonging.objects.all()
     serializer_class = serializers.BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
     queryset = models.Borrowed.objects.all()
     serializer_class = serializers.BorrowedSerializer
