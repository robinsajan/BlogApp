from django.db import models
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="profile/")
    name_for_blog = models.CharField(
        max_length=150, default="Tales Of Wasseypur")
    about_me = models.TextField()
    phone_no = models.CharField(max_length=10)
    instagram_url = models.URLField(default="", blank=True, null=True)
    linkeden_url = models.URLField(default="", blank=True, null=True)
    twitter_url = models.URLField(default="", blank=True, null=True)
    pitrest_url = models.URLField(default="", blank=True, null=True)
    dribble_url = models.URLField(default="", blank=True, null=True)
    website_url = models.URLField(default="", blank=True, null=True)
    github_url = models.URLField(default="", blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('about-page')


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    overview = models.TextField(max_length=300)
    body = RichTextUploadingField(
        help_text="<br>while adding images use percentages to get best Results")
    image = models.ImageField(null=True, blank=True, upload_to="posts/")
    date_posted = models.DateTimeField(default=timezone.now)
    tags = models.ForeignKey('Tags', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('article-view', kwargs={'pk': self.pk})


class Tags(models.Model):
    title = models.CharField(max_length=200, unique=True)
    context = models.TextField()
    image = models.ImageField(null=True, blank=True,
                              default="images/img3.png", upload_to="tag_title/")
    tag_bg_img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(Tags, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag-view', kwargs={'key': self.title})


class Comments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey('BlogPost', null=False, on_delete=models.CASCADE)
    comment = models.TextField()
    is_liked = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)


class Saved(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey('BlogPost', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
