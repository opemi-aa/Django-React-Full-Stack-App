from django.contrib import admin
from .models import Note, ActionLog

class ActionLogAdmin(admin.ModelAdmin):
    """
    Customizes the display for the ActionLog model in the Django admin site.
    """
    list_display = ('action_time', 'user', 'action_description', 'note_affected')
    list_filter = ('action_time', 'user')
    search_fields = ('action_description', 'user__username')
    readonly_fields = ('action_time', 'user', 'action_description', 'note_affected')

    def has_add_permission(self, request):
        # The audit log is append-only from the application logic.
        # No one should be able to add entries manually via the admin.
        return False

    def has_delete_permission(self, request, obj=None):
        # The audit log should be immutable.
        # No one should be able to delete entries.
        return False

# Register your models here.
admin.site.register(Note)
admin.site.register(ActionLog, ActionLogAdmin)