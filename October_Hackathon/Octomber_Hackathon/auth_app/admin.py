from django.contrib import admin
from Octomber_Hackathon.auth_app import models as auth_models


@admin.register(auth_models.AdvocateProfile)
class AdvocateProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(auth_models.AdvocateUser)
class AdvocateUserAdmin(admin.ModelAdmin):
    pass
