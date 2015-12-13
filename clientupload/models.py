from django.db import models
from django.utils import timezone
from authenticateclients.models import UploaderClient
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

#class UploaderClient(models.Model):
    #name = 'substitution'
    #nameOfCompany = models.CharField(max_length=100)
    #uploaderName = models.CharField(max_length=100)
    #pass

#Image Targets
def get_upload_imagetargetfile_name(instance, filename):
    return "%s/%s/ImageTargets/TargetFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_imageunitypackagefile_name(instance, filename):
    return "%s/%s/ImageTargets/UnityPackageFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_imageaugmentablecontentfile_name(instance, filename):
    return "%s/%s/ImageTargets/AugmentableContentFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_imageanalyticfile_name(instance, filename):
    return "%s/%s/ImageTargets/AnalyticsFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

#Object3DTargets
def get_upload_object3dtargetfile_name(instance, filename):
    return "%s/%s/Object3DTargets/TargetFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_object3dunitypackagefile_name(instance, filename):
    return "%s/%s/Object3DTargets/UnityPackageFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_object3daugmentablecontentfile_name(instance, filename):
    return "%s/%s/Object3DTargets/AugmentableContentFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_object3danalyticfile_name(instance, filename):
    return "%s/%s/Object3DTargets/AnalyticsFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

#Text
def get_upload_textaugmentablecontentfile_name(instance, filename):
    return "%s/%s/TextTargets/AugmentableContentFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

def get_upload_textanalyticfile_name(instance, filename):
    return "%s/%s/TextTargets/AnalyticsFile/%s" % (instance.uploaderclient.get_accountname(), instance.targetName, filename)

class ImageTarget(models.Model):
    #id is preexisting
    uploaderclient = models.ForeignKey('authenticateclients.UploaderClient', related_name='imagetargets')
    targetName = models.CharField(max_length=50, unique=True)
    imageWidth = models.IntegerField()

    #Actual Image Target File
    targetFile = models.FileField(upload_to=get_upload_imagetargetfile_name)
    #Unity Package File
    unityPackageFile = models.FileField(upload_to=get_upload_imageunitypackagefile_name, blank=True)
    
    #Augmentable content archive file
    augmentableZip = models.FileField(upload_to=get_upload_imageaugmentablecontentfile_name)

    #Analytics zip file
    analyticsZip = models.FileField(upload_to=get_upload_imageanalyticfile_name, blank=True)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ImageTarget, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.targetFile.delete(False)
        self.unityPackageFile.delete(False)
        self.augmentableZip.delete(False)
        self.analyticsZip.delete(False)
        super(ImageTarget, self).delete(*args, **kwargs)

    def __str__(self):
        return 'ImageTarget: {}'.format(self.targetName)

    def __unicode__(self):
        return self.targetName

class Object3DTarget(models.Model):
    #id is preexisting
    uploaderclient = models.ForeignKey('authenticateclients.UploaderClient', related_name='object3dtargets')
    targetName = models.CharField(max_length=50, unique=True)

    #Actual Image Target File
    targetFileZip = models.FileField(upload_to=get_upload_object3dtargetfile_name)
    #Unity Package File
    unityPackageFile = models.FileField(upload_to=get_upload_object3dunitypackagefile_name, blank=True)
    
    #Augmentable content archive file
    augmentableZip = models.FileField(upload_to=get_upload_object3daugmentablecontentfile_name)

    #Analytics zip file
    analyticsZip = models.FileField(upload_to=get_upload_object3danalyticfile_name, blank=True)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Object3DTarget, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.targetFileZip.delete(False)
        self.unityPackageFile.delete(False)
        self.augmentableZip.delete(False)
        self.analyticsZip.delete(False)
        super(Object3DTarget, self).delete(*args, **kwargs)

    def __str__(self):
        return 'Object3DTarget: {}'.format(self.targetName)

    def __unicode__(self):
        return self.targetName

class TextTarget(models.Model):
    #id is preexisting
    uploaderclient = models.ForeignKey('authenticateclients.UploaderClient', related_name='texttargets')
    targetName = models.CharField(max_length=50, unique=True)
    targetText = models.CharField(max_length=50)

    #Actual Image Target File
    #targetFile = models.FileField(upload_to='%s/%s/ImageTargetFile' % (UploaderClient, targetName))
    #Unity Package File
    #unityPackageFile = models.FileField(upload_to='%s/%s/UnityPackageFile' % (UploaderClient, targetName))
    #Augmentable content archive file
    augmentableZip = models.FileField(upload_to=get_upload_textaugmentablecontentfile_name)

    #Analytics zip file
    analyticsZip = models.FileField(upload_to=get_upload_textanalyticfile_name, blank=True)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TextTarget, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        #self.targetFile.delete(False)
        #self.unityPackageFile.delete(False)
        self.augmentableZip.delete(False)
        self.analyticsZip.delete(False)
        super(TextTarget, self).delete(*args, **kwargs)

    def __str__(self):
        return 'TextTarget: {}'.format(self.targetName)

    def __unicode__(self):
        return self.targetName

@receiver(pre_delete, sender=ImageTarget)
def imagetarget_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.targetFile.delete(False)
    instance.unityPackageFile.delete(False)
    instance.augmentableZip.delete(False)
    instance.analyticsZip.delete(False)

@receiver(pre_delete, sender=Object3DTarget)
def object3dtarget_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.targetFileZip.delete(False)
    instance.unityPackageFile.delete(False)
    instance.augmentableZip.delete(False)
    instance.analyticsZip.delete(False)


@receiver(pre_delete, sender=TextTarget)
def texttarget_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.augmentableZip.delete(False)
    instance.analyticsZip.delete(False)