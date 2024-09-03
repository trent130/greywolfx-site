from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from staticpages.models import Category, BlogPost, Profile, Employee, Comment, Testimonial, Subscribe, Director

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="tech",description="tech stuff")
    
    def  test_category_creation(self):
        self.assertEqual(self.category.name, "tech")
        self.assertEqual(self.category.description, "tech stuff")
    
    def test_category_str(self):
        self.assertEqual(str(self.category), "tech")

class BlogPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="username", password="password")
        self.category = Category.objects.create(name="tech", description="tech stuff")
        self.blogpost = BlogPost.objects.create(
            author = self.user,
            image = "test_image.png",
            title = "tech post",
            category = self.category,
            description = "test description"
        )
    def test_blogpost_creation(self):
        self.assertEqual(self.blogpost.author.username, "username")
        self.assertEqual(self.blogpost.category.name, "tech")
        self.assertEqual(self.blogpost.title, "tech post")
    
    def test_blogpost_str(self):
        self.assertEqual(str(self.blogpost), "tech post")

def ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="username", password="password")
        self.profile = Profile.objects.create(
            profile_picture = "test_profile.png",
            email = "test_email@example.org",
            user = self.user
        )
    def test_profile_creation(self):
        self.assertEqual(self.profile.profile_picture, "test_profile.png")
        self.assertEqual(self.profile.email, "test_email@example.org")
        self.assertEqual(self.profile.user.username, "username")
    
    def test_profile_str(self):
        self.assertEqual(str(self.profile), "username")

def CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="username", password="password")
        self.category = Category.objects.create(name="test", description="test description")
        self.profile = Profile.objects.create(
            user = self.user,
            bio = "test bio",
            profile_picture = "profile.png"
        )
        self.blogpost = BlogPost.objects.create(
            category = self.category,
            author = self.user,
            description = "test description",
            title = "test post",
            image = "test_image.png",
        )
        self.comment = Comment.objects.create(
            post = self.blogpost,
            content = "test comment",
            user = self.user,
            profile =self.profile,
        )
    
    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "test comment")
        self.assertEqual(self.comment.user.username, "username")
        self.assertEqual(self.comment.blogpost.title, "test post")
    
    def test_comment_str(self):
        self.assertEqual(str(self.comment), "username-test comment")
        
    def test_is_reply(self):
        self.assertFalse(self.comment.is_reply())

class TestimonialModelTest(TestCase):
    def setUp(self):
        self.testimonial = Testimonial.objects.create (
            name = "test user",
            picture = "test.png",
            feedback = "test feedback",
            post = "test post"
        )
    def test_testimonial_creation(self):
        self.assertEqual(self.testimonial.name, "test user")
        self.assertEqual(self.testimonial.post, "test post")
        
    def test_testimonial_str(self):
        self.assertEqual(str(self.testimonial), "test user")

class SubscribeModelTest(TestCase):
    def setUp(self):
        self.subscribe = Subscribe.objects.create(email="subscribe@example.org")
    
    def test_subscribe_creation(self):
        self.assertEqual(self.subscribe.email, "subscribe@example.org")
        
    def test_subscribe_str(self):
        self.assertEqual(str(self.subscribe), "subscribe@example.org")

class DirectorModelTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(
            director_name = "test name",
            director_email = "testname@example.org",
            director_picture = "test.png",
            director_post = "test post"
        )
    def test_director_creation(self):
        self.assertEqual(self.director.director_name, "test name")
        self.assertEqual(self.director.director_email, "testname@example.org")
        self.assertEqual(self.director.director_post, "test post")
    
    def test_director_str(self):
        self.assertEqual(str(self.director), "test name")
        
    def test_unique_together(self):
        Director.objects.create(director_name="test name", director_email="testname@example.org")
        
        with self.assertRaises(IntegrityError):
            Director.objects.create(director_name="test name", director_email="testname@example.org")

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="username", password="password")
        self.employee = Employee.objects.create(
            employee_name = "test name",
            employee_email = "testname@example.org",
            employee_picture = "test.png",
            employee_post = "test post",
            employee_age = 25,
            employee_gender = "male",
            employee_phone = "1234567890",
            employee_address = "test address",
            employee_dob = "1999-01-01"
        )
    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_name, "test name")
        self.assertEqual(self.employee.employee_email, "testname@example.org")
        self.assertEqual(self.employee.employee_post, "test post")
        
    def test_employee_str(self):
        self.assertEqual(str(self.employee), "test name")
