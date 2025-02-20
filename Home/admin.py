from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)

@admin.register(ClientMetadata)
class ClientMetadataAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'referrer', 'timestamp', "region_name")
    search_fields = ('ip_address', 'user_agent', 'referrer')

@admin.register(PostRequestMetadata)
class PostRequestMetadataAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'referrer', 'timestamp')
    search_fields = ('ip_address', 'user_agent', 'referrer', 'post_data')

@admin.register(ResumeViewMetadata)
class SpecialViewMetadataAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'referrer', 'view_name', "resume_region_name", 'timestamp')
    search_fields = ('ip_address', 'user_agent', 'referrer', 'view_name')