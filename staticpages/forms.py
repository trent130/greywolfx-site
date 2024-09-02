from django import forms
from django.contrib.auth.models import User
from .models import Comment, Profile, Subscribe

class signupForm(forms.ModelForm):
    """Form definition for signup."""
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control", "placeholder":"enter your password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control", "placeholder":"enter your password"}))
    
    class Meta:
        """Meta definition for signupform."""

        model = User
        fields = ('username', 'email', 'password1', 'password2')

class commentsForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for commentsform."""

        model = Comment
        fields = ("content", "parent")
        labels = {
            "content": "comment",
        }
        widgets = {
            "content": forms.Textarea(attrs={"class":"form-control", 'rows':2}),
            "parent": forms.HiddenInput(),
        }
    
class UserProfileForm(forms.ModelForm):
    """Form definition for UserProfile."""

    class Meta:
        """Meta definition for UserProfileform."""

        model = Profile
        fields = ('profile_picture', 'bio')
        
        widgets = {
            "profile_picture": forms.ClearableFileInput(attrs={"class":"form-control"}),
            "bio": forms.Textarea(attrs={"class":"form-control", "placeholder":"Limited by only our imagination", "size":5}),
        }


class ProfileForm(forms.ModelForm): 
	class Meta: 
		model = User 
		fields = ['username','first_name', 'last_name', 'email'] 
		labels = { 
			'username':'Username', 
			'first_name': 'First Name', 
			'last_name': 'Last Name', 
			'email': 'Email', } 
		widgets = { 
			'username': forms.TextInput(attrs={'class':'form-control'}), 
			'first_name': forms.TextInput(attrs={'class':'form-control'}), 
			'last_name':forms.TextInput(attrs={'class':'form-control'}), 
			'email': forms.TextInput(attrs={'class':'form-control'}), }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
        }