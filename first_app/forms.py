from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django.core.validators import validate_email

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'post_type', 'content', 'category', 'thumbnail_image']

        widgets = {
            'content': CKEditorUploadingWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment', 'rows': '5'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'parent_comment': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your reply', 'rows': '5'}),
        }


class ContactMeForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email address',
        validators=[validate_email],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail address'
        })
    )
    class Meta:
        model = ContactMe
        fields = ('first_name', 'last_name', 'email', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here', 'rows': '7'})
        }