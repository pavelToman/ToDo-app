from django.contrib import admin

# Register your models here.
from notes.models import List, Note


class NoteInline(admin.TabularInline):
    model = Note
    extra = 3


class ListAdmin(admin.ModelAdmin):
    inlines = [NoteInline]


admin.site.register(List, ListAdmin)
