from rest_framework import generics
from django.shortcuts import render
from .models import UserAuth
from .serializers import UserAuthSerializers

class UserAuthListCreateView(generics.ListCreateAPIView):
    querysets = UserAuth.objects.all()
    serializer_class = UserAuthSerializers

class UserAuthDetailView(generics.RetrieveUpdateDestroyAPIView):
    querysets = UserAuth.objects.all()
    serializer_class = UserAuthSerializers


def html_list_view(request):
    return render(request, 'master.html')
