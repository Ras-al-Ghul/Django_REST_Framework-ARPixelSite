from django.contrib import admin

from .models import ImageTarget, Object3DTarget, TextTarget

# Register your models here.
admin.site.register(ImageTarget)
admin.site.register(Object3DTarget)
admin.site.register(TextTarget)

