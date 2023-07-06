from django.contrib import admin
from Testapp.models import Gym_Member

# Register your models here.


class Gym_MemberAdmin(admin.ModelAdmin):
    list_display=['member_id','Name','email','password','mobile','is_active']

admin.site.register(Gym_Member,Gym_MemberAdmin)