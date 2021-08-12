from django.urls import path
from .views import HomeView, ArticleView, TagView, AllPostView, LikeCommentView, AddProfileView, EditProfileView, AddPostView, AddTagView, EditPostView, DeletePostView, EditTagView, DeleteTagView, SavePostView, AllSavedPost, DeleteCommentView, AboutPageView
urlpatterns = [
    path('', HomeView, name="home"),
    path('blogs/<int:pk>', ArticleView, name="article-view"),
    path('tags/<str:key>', TagView, name="tag-view"),
    path('all/blogs', AllPostView, name="all-blogs"),
    path('add/blogs/', AddPostView.as_view(), name="add-post"),
    path('edit/blogs/<int:pk>', EditPostView.as_view(), name="edit-post"),
    path('delete/blogs/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('add/tags/', AddTagView.as_view(), name="add-tags"),
    path('edit/tags/<int:pk>', EditTagView.as_view(), name="edit-tags"),
    path('delete/tags/<int:pk>', DeleteTagView.as_view(), name="delete-tags"),
    path('add/profile/', AddProfileView.as_view(), name="add-profile"),
    path('edit/profile/<int:pk>', EditProfileView.as_view(), name="edit-profile"),
    path('save/<int:pk>', SavePostView, name="save-post"),
    path('saved/blogs', AllSavedPost, name="all-saved-posts"),
    path('delete/comment/<int:pk>/<int:key>',
         DeleteCommentView, name="delete-comment"),
    path('about', AboutPageView, name="about-page"),
    path('like/<int:pk>', LikeCommentView, name="like-comment"),

]
