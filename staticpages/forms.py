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
        labels = {
            "username": "Username",
            "email": "email",
            "password1": "password",
            "password2": "confirm_password",
        }
        
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        username = self.cleaned_password.get("username")
        
        if password1 and password2 and password1 == password2:
            return form.ValidationError("password1 and password 2 are not the same")
            if len(password1) <= 10 and len(password2) <= 10:
                return forms.ValidationError("Password length should be 10 or more characters")
                if password1 and password2 and username and username in password1 :
                    return forms.ValidationError("you can not use the username as your password")        
        return password1
    
    def strong_pass(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        password = password1 and password2
        special_characters = ("@" "#", "$","%","&","*","(",")", "!")
        
        if password and any(char in special_characters for char in password):
            return forms.ValidationError("Password should contain at least one special character")
        return password1
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        return email
    
    def clean_username(self):
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

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
        
    def clean_comment(self):
        content = self.cleaned_data.get("content")
        if content == content:
            return forms.ValidationError("the same comment can not be returned")
        return content
    
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
            'email': 'Email', 
        } 

        widgets = { 
            'username': forms.TextInput(attrs={'class':'form-control'}), 
            'first_name': forms.TextInput(attrs={'class':'form-control'}), 
            'last_name':forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.TextInput(attrs={'class':'form-control'}), 
        }
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
            
        if username and first_name and last_name and username == first_name or username == last_name:
            return forms.ValidationError("username can not be the same as first name or last name")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email 
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name and first_name.isalpha() == False:
            raise forms.ValidationError("First name should contain only alphabets")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name and last_name.isalpha() == False:
            raise forms.ValidationError("Last name should contain only alphabets")
        return last_name
    

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
        }
        
    def clean_email(self):
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
            if email and Subscribe.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already subscribed")
        return email