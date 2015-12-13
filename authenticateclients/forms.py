"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authenticateclients.models import UploaderClient

class UploaderClientCreationForm(UserCreationForm):
    
    #A form that creates a user, with no privileges, from the given email and
    #password.
    

    def __init__(self, *args, **kargs):
        #del self.fields['username']
        super(UploaderClientCreationForm, self).__init__(*args, **kargs)
        

    class Meta:
        model = UploaderClient
        fields = ("email",)

class UploaderClientChangeForm(UserChangeForm):
    #A form for updating users. Includes all the fields on
    #the user, but replaces the password field with admin's
    #password hash display field.
    

    def __init__(self, *args, **kargs):
        #del self.fields['accountname']
        super(UploaderClientChangeForm, self).__init__(*args, **kargs)
        

    class Meta:
        model = UploaderClient
        fields = ("email",)
"""