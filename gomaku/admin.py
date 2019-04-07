from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name')    # 在后台列表下显示的字段
