from django.contrib import admin
from .models import Program, Student, Comment, Page, TaskResult
# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor_name', 'manager_name')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email')
    list_filter = ('role',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'rating', 'created_date', 'program')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'order', 'is_visible', 'updated_at')
    list_editable = ('order', 'is_visible')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TaskResult)
class TaskResultAdmin(admin.ModelAdmin):
    list_display = ('input_a', 'input_h', 'input_r', 'input_m', 'result_text', 'created_at')