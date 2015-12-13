from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail

# Create your models here.

class UploaderClient(models.Model):
    user = models.OneToOneField(User)
    company_name = models.CharField(_('company name'), max_length=100)
    #vuforiadb_name = models.CharField(_('vuforia database name'), max_length=100, blank=True)
    

    class Meta:
        verbose_name = _('uploaderclient')
        verbose_name_plural = _('uploaderclients')

    def __str__(self):
        return 'UploaderClient: {}'.format(self.user.username)
    
    def __unicode__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.user.username)

    def get_company_name(self):
        return self.company_name

    def get_accountname(self):
        return self.user.username

    def get_full_name(self):
        return self.user.username

    def get_short_name(self):
        return self.user.username

    """
    def email_user(self, subject, message, from_email=None):
        #Sends an email to this User.
        send_mail(subject, message, from_email, [self.email])
    """


    
