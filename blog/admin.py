from django.contrib import admin
from .models import Post, Comment 

# 1. رجیستر کردن مدل Post (تنظیمات ساده شده)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # فقط فیلدهایی که در مدل شما وجود دارند را نمایش می‌دهیم
    list_display = ('title', 'created_at') 
    search_fields = ('title', 'body')

# 2. رجیستر کردن مدل Comment (تنظیمات درست)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on') 
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments'] 

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    approve_comments.short_description = 'تایید نظرات انتخاب شده'