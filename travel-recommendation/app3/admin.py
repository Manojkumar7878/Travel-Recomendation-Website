from django.contrib import admin
from .models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "pasw", "email",)

admin.site.register(Signup)
# admin.site.register(MemberAdmin)
admin.site.register(Datas)
admin.site.register(Place)