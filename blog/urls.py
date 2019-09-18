
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # the name here is used to remove the contradiction. For example, there is an other app which also has the
    # method PostListView, to clear that the PostListView belongs to particular app. In our case here is blog app.
    # Since, we are using generic listview as a class therefore we have mentioned it as_view()
    
    path('about/', views.about, name='blog-about'),
     
    
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   
]
