from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ContactMe)
admin.site.register(ContactInformation)
admin.site.register(SocialAccount)
admin.site.register(Service)