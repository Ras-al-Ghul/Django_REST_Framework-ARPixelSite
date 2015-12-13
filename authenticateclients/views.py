from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from authenticateclients.models import UploaderClient
from authenticateclients.serializers import UploaderClientSerializer
from authenticateclients.permissions import IsOwnerOrNothing

#@csrf_exempt
class UploaderClientList(generics.ListAPIView):
    queryset = UploaderClient.objects.all()
    serializer_class = UploaderClientSerializer
    permission_classes = (permissions.IsAuthenticated,permissions.IsAdminUser,)

#@csrf_exempt
class UploaderClientDetail(generics.RetrieveAPIView):
    queryset = UploaderClient.objects.all()
    serializer_class = UploaderClientSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)