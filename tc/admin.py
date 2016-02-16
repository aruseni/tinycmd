from django.contrib import admin
from tc.models import CommandString

class CommandStringAdmin(admin.ModelAdmin):
    list_display = ("string_id", "datetime_added")
    list_filter = ("datetime_added",)
    search_fields = ["string_id", "command_string"]

admin.site.register(CommandString, CommandStringAdmin)
