from django.urls import path
from . import views 
from .views import dislike_thread
from .views import like_thread, likes
from .views import thread_detail



urlpatterns = [
    path('', views.index, name='index'),
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('newthread/', views.new_thread, name='new_thread'),
    path('thread/<int:thread_id>/update/', views.update_thread, name='update_thread'),
    path('thread/<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('thread/<int:thread_id>/reply/<int:reply_id>/update/', views.update_reply, name='update_reply'),
    path('thread/<int:thread_id>/reply/<int:reply_id>/delete/', views.delete_reply, name='delete_reply'),
    path('threads/update_likes/', views.update_likes, name='update_likes'),
    path('like/<int:thread_id>/', like_thread, name='like_thread'),
    path('likes/', likes, name='likes'),
    path('dislike/<int:thread_id>/', dislike_thread, name='dislike_thread'),
    path('thread/<int:pk>/', thread_detail, name='thread_detail'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread'),
]