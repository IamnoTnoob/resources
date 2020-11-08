from django.contrib import admin
from accounts.models import Profile

# Register your models here.

admin.site.site_header = "noTnoob Dashboard"
admin.site.site_title = "noTnoob"
admin.site.index_title = "noTnoob"


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)