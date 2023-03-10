from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField



#models
class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profession_choices = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('engineer', 'Engineer'),
        ('doctor', 'Doctor'),
        ('lawyer', 'Lawyer'),
        ('business', 'Business'),
        ('other', 'Other'),
    ]
    profession = models.CharField(max_length=255, choices=profession_choices, blank=True, null=True)
    country = CountryField(default='BD')
    division = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    thana = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.email
    

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, username, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_TYPE_CHOICES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    title = models.CharField(max_length=255)
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='article')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title
    

    def increment_view_count(self):
        self.view_count += 1
        self.save()


    def increment_comment_count(self):
        self.comment_count += 1
        self.save()


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f'{self.name} - {self.post.title}'
    

class ContactMe(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

    class Meta:
        verbose_name_plural = 'Contact Me'


class ContactInformation(models.Model):
    email = models.EmailField()
    mobile = PhoneNumberField()
    location = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.URLField()


    def __str__(self):
        return self.email


class SocialAccount(models.Model):
    SOCIAL_CHOICE = (
        ('', '--- Select Social Media ---'),
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('LinkedIn', 'LinkedIn'),
        ('YouTube', 'YouTube'),
        ('Instagram', 'Instagram'),
        ('Pintarest', 'Pintarest'),
        ('GitHub', 'GitHub'),
    )
    media_name = models.CharField(max_length=255, choices=SOCIAL_CHOICE)
    profile_url = models.URLField()

    class Meta:
        verbose_name = "Social Account"
        verbose_name_plural = "Social Accounts"
    
    def __str__(self):
        return self.media_name
    



class Service(models.Model):
    service_name = models.CharField(max_length=120)
    icon = models.ImageField(upload_to='service')
    short_description = models.TextField()
    details = RichTextUploadingField()


    def __str__(self) -> str:
        return self.service_name
    

    class Meta:
        verbose_name_plural = "Service"