from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Admin Courses"
admin.site.site_title = "DEVELOP YOURSELF!"
admin.site.index_title = "Welcom to our courses"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
