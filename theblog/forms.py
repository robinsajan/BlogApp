from django import forms
from django.forms import fields, widgets
from .models import BlogPost, Profile, Tags, Comments


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'overview', 'body', 'image', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'overview': forms.Textarea(attrs={'rows': 3, 'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'tags': forms.Select(attrs={'class': "form-control"}),
        }


class TagsForm(forms.ModelForm):

    class Meta:
        model = Tags
        fields = ('title', 'context', 'image', 'tag_bg_img')
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'context': forms.Textarea(attrs={'rows': 3, 'class': "form-control"}),
        }


class CommentsForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={
                           'value': ' ', 'id': 'user-box-forum', 'class': 'form-control', 'type': 'hidden'}))
    post = forms.CharField(widget=forms.TextInput(attrs={
                           'value': ' ', 'id': 'q-box-forum', 'class': 'form-control', 'type': 'hidden'}))
    comment = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Add a Comment', 'class': 'text-area'}))


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('user', 'image', 'name_for_blog', 'about_me', 'phone_no', 'instagram_url',
                  'linkeden_url', 'twitter_url', 'pitrest_url', 'dribble_url', 'website_url')

        widgets = {
            'user': forms.TextInput(attrs={'value': ' ', 'id': 'user-box', 'type': 'hidden', 'class': 'form-control'}),
            'name_for_blog': forms.TextInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'row': 4, 'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkeden_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'pitrest_url': forms.URLInput(attrs={'class': 'form-control'}),
            'dribble_url': forms.URLInput(attrs={'class': 'form-control'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control'})
        }
