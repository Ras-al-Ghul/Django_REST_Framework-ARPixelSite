from rest_framework import serializers
from authenticateclients.models import UploaderClient

from authenticateclients.serializers import UploaderClientSerializer
from clientupload.models import ImageTarget, Object3DTarget, TextTarget

class ImageTargetSerializer(serializers.HyperlinkedModelSerializer):

	uploaderclient = UploaderClientSerializer(read_only=True,required=False)

	targetFile = serializers.FileField(label='TargetFile')
	unityPackageFile = serializers.FileField(label='UnityPackageFile', allow_null=True, required=False)
	augmentableZip = serializers.FileField(label='AugmentableZip')
	analyticsZip = serializers.FileField(label='AnalyticsZip', allow_null=True, required=False)

	url = serializers.HyperlinkedIdentityField(view_name='imagetargetsdetail')

	class Meta:
		model = ImageTarget
		fields = ('url','uploaderclient','targetName','imageWidth','targetFile','unityPackageFile','augmentableZip','analyticsZip')

	def get_validation_exclusions(self):
		exclusions = super(ImageTargetSerializer, self).get_validation_exclusions()
		return exclusions + ['uploaderclient']

	def create(self, attrs, instance=None):
		if instance is not None:
			instance.targetName = attrs.get('targetName', instance.targetName)
			instance.imageWidth = attrs.get('imageWidth', instance.imageWidth)
			instance.targetFile = attrs.get('targetFile', instance.targetFile)
			instance.unityPackageFile = attrs.get('unityPackageFile', instance.unityPackageFile)
			instance.augmentableZip = attrs.get('augmentableZip', instance.augmentableZip)
			instance.analyticsZip = attrs.get('analyticsZip', instance.analyticsZip)
			return instance

		imagetarget = ImageTarget.objects.create(uploaderclient=attrs.get('uploaderclient') ,targetName=attrs.get('targetName'), imageWidth= attrs.get('imageWidth'), targetFile=attrs.get('targetFile'), unityPackageFile=attrs.get('UnityPackageFile'), augmentableZip=attrs.get('augmentableZip'), analyticsZip=attrs.get('analyticsZip'),)
		return imagetarget

class Object3DTargetSerializer(serializers.HyperlinkedModelSerializer):

	uploaderclient = UploaderClientSerializer(read_only=True,required=False)

	targetFileZip = serializers.FileField(label='TargetFileZip')
	unityPackageFile = serializers.FileField(label='UnityPackageFile', allow_null=True, required=False)
	augmentableZip = serializers.FileField(label='AugmentableZip')
	analyticsZip = serializers.FileField(label='AnalyticsZip', allow_null=True, required=False)

	url = serializers.HyperlinkedIdentityField(view_name='object3dtargetsdetail')

	class Meta:
		model = Object3DTarget
		fields = ('url','uploaderclient','targetName','targetFileZip','unityPackageFile','augmentableZip','analyticsZip')

	def get_validation_exclusions(self):
		exclusions = super(Object3DTargetSerializer, self).get_validation_exclusions()
		return exclusions + ['uploaderclient']

	def create(self, attrs, instance=None):
		if instance is not None:
			instance.targetName = attrs.get('targetName', instance.targetName)
			instance.targetFile = attrs.get('targetFileZip', instance.targetFile)
			instance.unityPackageFile = attrs.get('unityPackageFile', instance.unityPackageFile)
			instance.augmentableZip = attrs.get('augmentableZip', instance.augmentableZip)
			instance.analyticsZip = attrs.get('analyticsZip', instance.analyticsZip)
			return instance

		object3dtarget = Object3DTarget.objects.create(uploaderclient=attrs.get('uploaderclient') ,targetName=attrs.get('targetName'), targetFileZip=attrs.get('targetFileZip'), unityPackageFile=attrs.get('UnityPackageFile'), augmentableZip=attrs.get('augmentableZip'), analyticsZip=attrs.get('analyticsZip'),)
		return object3dtarget

class TextTargetSerializer(serializers.ModelSerializer):

	uploaderclient = UploaderClientSerializer(read_only=True,required=False)

	augmentableZip = serializers.FileField(label='AugmentableZip')
	analyticsZip = serializers.FileField(label='AnalyticsZip', allow_null=True, required=False)

	url = serializers.HyperlinkedIdentityField(view_name='texttargetsdetail')

	class Meta:
		model = TextTarget
		fields = ('url','uploaderclient','targetName','targetText','augmentableZip','analyticsZip')

	def get_validation_exclusions(self):
		exclusions = super(TextTargetSerializer, self).get_validation_exclusions()
		return exclusions + ['uploaderclient']

	def create(self, attrs, instance=None):
		if instance is not None:
			instance.targetName = attrs.get('targetName', instance.targetName)
			instance.targetText = attrs.get('targetText', instance.targetName)
			instance.augmentableZip = attrs.get('augmentableZip', instance.augmentableZip)
			instance.analyticsZip = attrs.get('analyticsZip', instance.analyticsZip)
			return instance

		texttarget = TextTarget.objects.create(uploaderclient=attrs.get('uploaderclient') ,targetName=attrs.get('targetName'),targetText=attrs.get('targetText'), augmentableZip=attrs.get('augmentableZip'), analyticsZip=attrs.get('analyticsZip'),)
		return texttarget

