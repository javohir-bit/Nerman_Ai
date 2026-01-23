from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'icon', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['question', 'answer', 'keywords']
    list_editable = ['is_active']
    ordering = ['category', '-created_at']
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('category', 'icon', 'question', 'answer')
        }),
        ('Qidiruv', {
            'fields': ('keywords',)
        }),
        ('Holat', {
            'fields': ('is_active',)
        }),
    )
