from django.contrib import admin
from .models import BlogPost, Comment, Category, Profile, Subscribe, Testimonial, Director

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'likes', 'category', 'time_uploaded')
    ordering = ['-time_uploaded']
    search_fields = ['author', 'category', 'time_uploaded']
admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_uploaded')
    search_fields = ['user__username',]
    ordering = ['-time_uploaded']
admin.site.register(Comment, CommentAdmin)
    
admin.site.register(Category)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date', )
    search_fields = ['name', 'post']
    ordering = ['-date']
admin.site.register(Testimonial, TestimonialAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')
admin.site.register(Profile)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ['email']
    ordering = ['-date_subscribed']
admin.site.register(Subscribe, SubscribeAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('director_name', 'director_post', 'director_email', 'date_added')
    list_filter = ['director_post', 'director_email']
    search_fields = ['director_post', 'director_name', 'director_email']
    ordering = ['-date_added']

admin.site.register(Director, DirectorAdmin)
    