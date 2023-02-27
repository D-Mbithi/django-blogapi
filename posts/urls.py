from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListApiView.as_view(), name="post_list"),
    path('<int:pk>', views.PostDetailApiView.as_view(), name="post_detail"),
]
