from django.contrib import admin
from .models import CodeSnippet

class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'address', 'link')
    search_fields = ('code', 'address')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)  # Робимо поле лише для читання

admin.site.register(CodeSnippet, CodeSnippetAdmin)