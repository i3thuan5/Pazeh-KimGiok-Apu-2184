from django.contrib import admin
from autai.models import Record


class RecordAdmin(admin.ModelAdmin):
    search_fields = ('pazeh', 'hua')
    ordering = ('csvid', 'pageid',)

    list_display = ('csvid', 'pazeh', 'hua',)

# Register your models here.
admin.site.register(Record, RecordAdmin)


admin.site.site_header = '潘金玉《巴宰族母語錄音2184句》數位化網站'
admin.site.index_title = '網站管理'
