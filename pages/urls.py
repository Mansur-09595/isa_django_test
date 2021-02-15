from django.urls import path

from. import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.UpdatePostView.as_view(), name='post_edit'),
    path('about/', views.About.as_view(), name='about'),
]
