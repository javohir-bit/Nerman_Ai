from django.db import models
from django.utils import timezone


class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('platform', '🛠 Platforma'),
        ('video', '🎬 Video va montaj'),
        ('ai', '🤖 Sun\'iy intellekt'),
        ('account', '🔐 Akkaunt va kirish'),
        ('payment', '💳 To\'lovlar'),
        ('other', '🧪 Boshqa'),
    ]
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='Kategoriya'
    )
    icon = models.CharField(
        max_length=10,
        default='❓',
        verbose_name='Icon'
    )
    question = models.CharField(
        max_length=255,
        verbose_name='Savol'
    )
    answer = models.TextField(
        verbose_name='Javob'
    )
    keywords = models.TextField(
        help_text='Qidiruv uchun kalit so\'zlar (vergul bilan ajrating)',
        verbose_name='Kalit so\'zlar'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Aktiv'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yaratilgan'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Yangilangan'
    )
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['category', '-created_at']
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.question}"
    
    def get_keywords_list(self):
        return [kw.strip().lower() for kw in self.keywords.split(',')]
