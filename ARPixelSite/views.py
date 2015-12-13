from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authenticateclients.models import UploaderClient
from authenticateclients.serializers import UploaderClientSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from clientupload.models import ImageTarget, Object3DTarget, TextTarget
from clientupload.serializers import ImageTargetSerializer, Object3DTargetSerializer, TextTargetSerializer
from clientupload.permissions import IsOwnerOrNothing

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'uploaderclients': reverse('uploaderclient-list', request=request, format=format),
        'imagetargets': reverse('imagetarget-list', request=request, format=format)
    })