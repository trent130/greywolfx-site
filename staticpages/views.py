from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import signupForm, commentsForm, ProfileForm, UserProfileForm, SubscribeForm
from .models import BlogPost, Comment, Profile, Category, Subscribe, Testimonial
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.views.generic import DetailView
from django.utils import timezone
from django.db.models import Count


# Create your views here.
def index(request):
    return render(request, "staticpages/index.html")

def about(request):
    return render(request, "staticpages/about.html")

def contact(request):
    return render(request, "staticpages/contact.html")

def privacy_policy(request):
    return render(request, "staticpages/privacy_policy.html")

def services(request):
    return render(request, "staticpages/services.html")

def term_conditions(request):
    return render(request, "staticpages/empty.html")

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                messages.error(request, "user with the email already exist")
                return HttpResponseRedirect(reverse("staticpages:signup"))
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            
            messages.success(request, "Registration successful")
            login(request, user)
            return HttpResponseRedirect(reverse("staticpages:signup"))
        else:
            messages.error(request, "invalid form")
            return HttpResponseRedirect(reverse("staticpages:signup"))
    else:
        form = signupForm()
    context = {'form':form}
    return render(request, "registration/signup.html", context)

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-time_uploaded')

    
    paginator = Paginator(posts, 12)  # Show 12 blogs per page.

    url = reverse('staticpages:blog_list')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'url':url,}
    return render(request, "staticpages/blog.html", context)

@login_required
def blog_details(request, pk):
    try:
        post = get_object_or_404(BlogPost, pk=pk)
        comments = post.comments.filter(parent__isnull=True)
        new_comment = None
        
        form = commentsForm()
        subscribe_form = SubscribeForm()
        
        if request.method == "POST":
            if 'comment_submit' in request.POST:
                comment_form = commentsForm(request.POST)
                if comment_form.is_valid():
                    new_comment = comments_form.save(commit=False)
                    new_comment.user = request.user
                    new_comment.profile = request.user.profile
                    new_comment.post = post
                    new_comment.save()
                    form = commentsForm()
                    return HttpResponseRedirect(reverse('staticpages:blog_detail', args=[pk]))
                else:
                    messages.error(request, "Invalid comment form")
            elif 'subscribe_submit' in request.POST:
                subscribe_form = SubscribeForm(request.POST)
                if subscribe_form.is_valid():
                    subscribe_form.save()
                    messages.success(request, "You have successfully subscribed!")
                else:
                    messages.error(request, "Invalid email for subscription")
            
            return HttpResponseRedirect(reverse("staticpages:blog_detail", args=[pk]))
        
        now = timezone.now()
        one_week_ago = now - timedelta(days=7)
        
        top_stories = BlogPost.objects.filter(time_uploaded__gte=one_week_ago).order_by('-likes')[:3]
        
        context = {
            "title": "blog_detail",
            "form": form,
            "subscribe_form": subscribe_form,
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "top_stories": top_stories,
        }
        return render(request, "staticpages/single.html", context)
    
    except BlogPost.DoesNotExist:
        return HttpResponse("Blog does not exist", status=404)

def category_items(request, id):
    category = get_object_or_404(Category, id=id)
    category_posts = BlogPost.objects.filter(category=category)
    context = {"title":"category_items", "category":category, "category_posts":category_posts}
    return render(request, "staticpages/category_items.html", context)
    
@login_required   
def ProfileView(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
    
        if form.is_valid():
            profile_form.save()
            form_save()
            
            messages.success(request, "profile updated successful")
            return HttpResponseRedirect(reverse("staticpages:profile"))
        else:
            return HttpResponseRedirect(reverse("staticpages:profile"))
    else:
        profile_form = ProfileForm(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=profile)
    context = {"title":"profile", "form":form, "profile":profile, "profile_form":profile_form}
    return render(request, "staticpages/profile.html", context)

@login_required
def Employeeview(request):
    pass
    