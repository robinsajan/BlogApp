from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .models import BlogPost, Profile, Tags, Comments, Saved
import random
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import BlogPostForm, ProfileForm, TagsForm, CommentsForm
from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser

# Create your views here.


def HomeView(request):
    try:
        admin = get_user_model().objects.get(is_superuser=True)
    except get_user_model().DoesNotExist:
        admin = False
    all_post = BlogPost.objects.all()
    all_posts = []
    for ap in all_post:
        all_posts.append(ap.title)
    user_count = get_user_model().objects.all().count()
    posts = BlogPost.objects.all().order_by('-date_posted')[:4]
    tags = Tags.objects.all().order_by('title')
    post = Tags.objects.all().count()
    all_id = Tags.objects.all()
    all_keys = []
    for all in all_id:
        all_keys.append(all.id)
    list = []
    while(len(list) < post):
        if len(list) < 5:
            n = random.choices(all_keys)
            if n[0] not in list:
                list.append(n[0])
        else:
            break

    try:
        one = Tags.objects.get(pk=list[0])
    except Tags.DoesNotExist:
        one = False
    except IndexError:
        one = False
    try:
        two = Tags.objects.get(pk=list[1])
    except Tags.DoesNotExist:
        two = False
    except IndexError:
        two = False
    try:
        three = Tags.objects.get(pk=list[2])
    except Tags.DoesNotExist:
        three = False
    except IndexError:
        three = False
    try:
        four = Tags.objects.get(pk=list[3])
    except Tags.DoesNotExist:
        four = False
    except IndexError:
        four = False
    try:
        five = Tags.objects.get(pk=list[4])
    except Tags.DoesNotExist:
        five = False
    except IndexError:
        five = False

    popular = Comments.objects.values('post').annotate(
        dcount=Count('id')).order_by('-dcount')[:3]
    p_list = []
    for p in popular:
        p_list.append(p.get("post"))

    try:
        p_one = BlogPost.objects.get(pk=p_list[0])
    except BlogPost.DoesNotExist:
        p_one = False
    except IndexError:
        p_one = False
    try:
        p_two = BlogPost.objects.get(pk=p_list[1])
    except BlogPost.DoesNotExist:
        p_two = False
    except IndexError:
        p_two = False
    try:
        p_three = BlogPost.objects.get(pk=p_list[2])
    except BlogPost.DoesNotExist:
        p_three = False
    except IndexError:
        p_three = False
    context = {
        'posts': posts,
        'tags': tags,
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five,
        'p_one': p_one,
        'p_two': p_two,
        'p_three': p_three,
        'user_count': user_count,
        'all_posts': all_posts,
        'admin': admin,


    }
    return render(request, 'main.html', context)


def SavePostView(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    user = request.user
    saveit = Saved(user=user, post=post)
    saveit.save()

    return redirect("article-view", pk)


def AboutPageView(request):
    admin = get_user_model().objects.get(is_superuser=True)
    tags = Tags.objects.all().order_by('title')

    context = {
        'admin': admin,
        'tags': tags,
    }
    return render(request, 'about_view.html', context)


def LikeCommentView(request, pk):
    comment = Comments.objects.get(id=pk)
    comment.is_liked = True
    comment.save()

    return redirect("article-view", comment.post.id)


def ArticleView(request, pk):
    #post = BlogPost.objects.get(pk=pk)
    admin = get_user_model().objects.get(is_superuser=True)
    post = get_object_or_404(BlogPost, pk=pk)
    tag = BlogPost.objects.get(pk=pk).tags
    tags = Tags.objects.all().order_by('title')
    comments_count = Comments.objects.filter(post=post).count()
    try:
        related_post = BlogPost.objects.filter(~Q(pk=pk)).filter(
            tags=tag).order_by('-date_posted')[:5]
    except BlogPost.DoesNotExist:
        related_post = False
    try:
        comments = Comments.objects.filter(post=post).order_by('-date_posted')
    except Comments.DoesNotExist:
        comments = False

    try:
        if not request.user.is_authenticated:
            is_saved = False
        else:
            is_saved = Saved.objects.filter(user=request.user, post=post)
    except Saved.DoesNotExist:
        is_saved = False
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        comment = request.POST['comment']
        r = Comments(user=request.user, post=post, comment=comment)
        form = CommentsForm()
        r.save()

        return redirect("article-view", pk)
    else:
        form = CommentsForm()
    context = {
        'post': post,
        'tag': tag,
        'tags': tags,
        'related_post': related_post,
        'comments': comments,
        'form': form,
        'is_saved': is_saved,
        'admin': admin,
        'comments_count': comments_count,

    }
    return render(request, 'article_view.html', context)


def DeleteCommentView(request, pk, key):
    comment = Comments.objects.get(id=key)
    comment.delete()

    return redirect('article-view', pk)


def AllSavedPost(request):
    posts = Saved.objects.filter(user=request.user)
    admin = get_user_model().objects.get(is_superuser=True)
    tags = Tags.objects.all().order_by('title')
    context = {
        'posts': posts,
        'tags': tags,
        'admin': admin,
    }
    return render(request, 'saved_posts_view.html', context)


def AllPostView(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    tags = Tags.objects.all().order_by('title')
    admin = get_user_model().objects.get(is_superuser=True)
    context = {
        'posts': posts,
        'tags': tags,
        'admin': admin,
    }
    return render(request, 'all_post.html', context)


def TagView(request, key):
    tag = Tags.objects.get(title=key.replace('-', ' '))
    tags = Tags.objects.all().order_by('title')
    posts = BlogPost.objects.filter(tags=tag)
    post_count = BlogPost.objects.filter(tags=tag).count()
    admin = get_user_model().objects.get(is_superuser=True)
    context = {
        'tag': tag,
        'tags': tags,
        'posts': posts,
        'post_count': post_count,
        'admin': admin,
    }
    return render(request, 'tag_list.html', context)

# --------------PROFILE---------------------


class AddProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'add_profile.html'


class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
# --------------BLOGPOST-----------------


class AddPostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'add_post.html'


class EditPostView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
# ------------------TAGS--------------------


class AddTagView(CreateView):
    model = Tags
    form_class = TagsForm
    template_name = 'add_tags.html'


class EditTagView(UpdateView):
    model = Tags
    form_class = TagsForm
    template_name = 'edit_tags.html'


class DeleteTagView(DeleteView):
    model = Tags
    template_name = 'delete_tag.html'
    success_url = reverse_lazy('home')
