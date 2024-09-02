from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

def default_category():
    category, created = Category.objects.get_or_create(name="Default")
    return category.id
 
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog_images")
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_uploaded = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pictures")
    bio = models.TextField()
    
    def __str__(self):
        return self.user.first_name
    
@receiver(post_save, sender=User)
def create_user_related_profiles(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, "profile"):
            instance.profile.save()
            
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    time_uploaded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.user.username}-{self.content[:30]}"
    
    def is_reply(self):
        return self.parent is not None

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="Testimonial_pictures", null=True, blank=True)
    feedback = models.TextField()
    post = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    director_post = models.CharField(max_length=50)
    director_picture = models.ImageField(upload_to="director_pics")
    director_email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class meta:
        # constraints = [
        #     models.CheckConstraints(check = models.Q(age__gte=18), name="age__gte__18")
        # ]
        unique_together = ('director_email', 'director_name')
        
    def __str__(self):
        return self.director_name # TODO