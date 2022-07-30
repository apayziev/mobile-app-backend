from django.contrib import admin
from course.models import Course, Category, CourseAuthor
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'rating', 'enrolment_count', 'level', 'status', 'duration')
    list_filter = ('category', 'author', 'rating', 'enrolment_count', 'level', 'status', 'duration')
    search_fields = ('title', 'category', 'author', 'rating', 'enrolment_count', 'level', 'status', 'duration')
    ordering = ('title', 'category', 'rating','level', 'status', 'duration')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CourseAuthor)
class CourseAuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job')
    search_fields = ('first_name', 'last_name', 'job')
    ordering = ('first_name', 'last_name', 'job')