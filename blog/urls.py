from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    ProfileDetailView,
    profile_edit,
    SearchView,
    CategoryListView,
    register,
    LikeView,
    update_comment,
    delete_comment,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<str:category>/', CategoryListView.as_view(), name='category-posts'),
    path('register/', register, name='register'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('comment/update/<int:pk>/', update_comment, name='update-comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete-comment'),
]
