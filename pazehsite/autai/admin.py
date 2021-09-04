from django.contrib import admin
from autai.models import Record


class RecordAdmin(admin.ModelAdmin):
    search_fields = ('pazeh', 'hua')
    ordering = ('csvid', 'pageid',)

    list_display = ('csvid', 'pazeh', 'hua',)

# Register your models here.
admin.site.register(Record, RecordAdmin)
