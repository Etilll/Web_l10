from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.my_posts, name="post"),
    path("add_post/", views.PostCreateView.as_view(), name="add_post"),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="post_delete"),
    path("register/", views.register, name="register"), 
    path ("authors/", views.authors, name="authors"),
    path("authors/<int:author_id>/", views.author_details, name="author_details"),
    path("add_author/", views.AuthorCreateView.as_view(), name="add_author"),
    path("author/<int:pk>/update", views.AuthorUpdateView.as_view(), name="author_update"),
    path("author/<int:pk>/delete", views.AuthorDeleteView.as_view(), name="author_delete"),
    path ("tags/", views.tags, name="tags"),
    path("tags/<int:tag_id>/", views.tag_details, name="tag_details"),
    path("add_tag/", views.TagCreateView.as_view(), name="add_tag"),
    path("tag/<int:pk>/update", views.TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete", views.TagDeleteView.as_view(), name="tag_delete"),
]