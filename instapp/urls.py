from django.urls import path, include
from . import views

urlpatterns = [
    path('post', views.post, name='post'),
    path('<int:image_id>', views.imagedetail, name='imagedetail'),
    path('<int:image_id/like>', views.like, name='like'),
    path('profile', views.profile_index, name='profile'),
]
