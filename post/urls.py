from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetPosts, name='get_all_posts'),
    path("<slug:slug>/",views.GetSinglePost,name="get_single_post"),
    path("add/",views.AddPost,name="add_post"),
    path("update/<int:id>",views.UpdatePost,name="update_post"),
    path("delete/<int:id>",views.DeletePost,name="delete_post"),
    path("comments/<slug:slug>/",views.GetComments,name="get_comments"),
]