from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from authenticateclients.serializers import UploaderClientSerializer
from authenticateclients.models import UploaderClient
from clientupload.models import ImageTarget, Object3DTarget, TextTarget
from clientupload.serializers import ImageTargetSerializer, Object3DTargetSerializer, TextTargetSerializer
from clientupload.permissions import IsOwnerOrNothing


#@csrf_exempt
class ImageTargetList(generics.ListCreateAPIView):
	queryset = ImageTarget.objects.all()
	serializer_class = ImageTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

	def list(self, request):
		newqueryset = self.get_queryset()
		queryset = []
		for i in newqueryset:
			if i.uploaderclient.user == self.request.user:
				queryset.append(i)
		serializer = ImageTargetSerializer(queryset, many=True, context={'request':request})
		return Response(serializer.data)

	def perform_create(self, serializer):
		uploaderclientarray = UploaderClient.objects.all()
		for i in uploaderclientarray:
			if i.user == self.request.user:
				instance = serializer.save(uploaderclient=i)
	
#@csrf_exempt
class ImageTargetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ImageTarget.objects.all()
	serializer_class = ImageTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

class Object3DTargetList(generics.ListCreateAPIView):
	queryset = Object3DTarget.objects.all()
	serializer_class = Object3DTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

	def list(self, request):
		newqueryset = self.get_queryset()
		queryset = []
		for i in newqueryset:
			if i.uploaderclient.user == self.request.user:
				queryset.append(i)
		serializer = Object3DTargetSerializer(queryset, many=True, context={'request':request})
		return Response(serializer.data)

	def perform_create(self, serializer):
		uploaderclientarray = UploaderClient.objects.all()
		for i in uploaderclientarray:
			if i.user == self.request.user:
				instance = serializer.save(uploaderclient=i)
	
#@csrf_exempt
class Object3DTargetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Object3DTarget.objects.all()
	serializer_class = Object3DTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

class TextTargetList(generics.ListCreateAPIView):
	queryset = TextTarget.objects.all()
	serializer_class = TextTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

	def list(self, request):
		newqueryset = self.get_queryset()
		queryset = []
		for i in newqueryset:
			if i.uploaderclient.user == self.request.user:
				queryset.append(i)
		serializer = TextTargetSerializer(queryset, many=True, context={'request':request})
		return Response(serializer.data)

	def perform_create(self, serializer):
		uploaderclientarray = UploaderClient.objects.all()
		for i in uploaderclientarray:
			if i.user == self.request.user:
				instance = serializer.save(uploaderclient=i)
	
#@csrf_exempt
class TextTargetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = TextTarget.objects.all()
	serializer_class = TextTargetSerializer
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrNothing,)

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'uploaderclients': reverse('uploaderclients', request=request, format=format),
        'imagetargets': reverse('imagetargets', request=request, format=format),
        'object3dtargets': reverse('object3dtargets', request=request, format=format),
        'texttargets': reverse('texttargets', request=request, format=format),
    })