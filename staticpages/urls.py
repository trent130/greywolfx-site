from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'staticpages'

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("terms", views.term_conditions, name="term_conditions"),
    path("privacy", views.privacy_policy, name="privacy_policy"),
    path("services", views.services, name="services"),
    path("about", views.about, name="about"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("signup", views.signup, name="signup"),
    path("blog_list", views.blog_list, name="blog_list"),
    path("blog/<int:pk>/", views.blog_details, name="blog_detail"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("profile", views.ProfileView, name="profile"),
    path("category/<int:id>/", views.category_items, name="category_items")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)