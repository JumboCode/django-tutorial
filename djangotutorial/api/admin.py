from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

#
#   Define Admin Interface for Accounts
#

class SledAdmin(admin.ModelAdmin):
    list_display = ('name', 'victories', 'defeats')
    readonly_fieds = ['victories', 'defeats']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("sled", "captain", "first_name", "last_name", "phone_number")









admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Sled, SledAdmin)
