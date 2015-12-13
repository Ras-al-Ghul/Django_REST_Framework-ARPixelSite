from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authenticateclients.models import UploaderClient

from clientupload.models import ImageTarget

class UploaderClientSerializer(serializers.HyperlinkedModelSerializer):
	
	username = serializers.CharField(source='user.username')
	email = serializers.CharField(source='user.email', required=False, allow_null=True)
	password = serializers.CharField(source='user.password', write_only=True, required=False)
	#confirm_password = serializers.CharField(write_only=True, required=False)
	date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
	last_login = serializers.DateTimeField(source='user.last_login', read_only=True)

	company_name = serializers.CharField()

	imagetargets = serializers.HyperlinkedRelatedField(many=True, view_name='imagetargetsdetail', read_only=True)
	object3dtargets = serializers.HyperlinkedRelatedField(many=True, view_name='object3dtargetsdetail', read_only=True)
	texttargets = serializers.HyperlinkedRelatedField(many=True, view_name='texttargetsdetail', read_only=True)

	url = serializers.HyperlinkedIdentityField(view_name='uploaderclientsdetail')

	class Meta:
		model = UploaderClient
		fields = ('url', 'email', 'username', 'company_name', 'date_joined', 'last_login', 'password','imagetargets','object3dtargets','texttargets',)
		read_only_fields = ('user.date_joined', 'user.last_login',)

	def create(self, attrs, instance=None):
		if instance is not None:
			instance.username = attrs.get('user.username', instance.user.username)
			instance.user.email = attrs.get('user.email', instance.user.email)
			instance.company_name = attrs.get('company_name', instance.company_name)
			instance.user.password = attrs.get('user.password', instance.user.password)
			return instance

		user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
		instance = UploaderClient.objects.create(company_name=attrs.get('company_name'),user=user)
		return instance

	def update(self, attrs, instance=None):
		if instance is not None:
			instance.username = attrs.get('user.username', instance.user.username)
			instance.user.email = attrs.get('user.email', instance.user.email)
			instance.company_name = attrs.get('company_name', instance.company_name)
			instance.user.password = attrs.get('user.password', instance.user.password)
			return instance

		user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
		return UploaderClient(user=user)

	