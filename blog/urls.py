from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/comment/', BlogCommentView.as_view(), name='blog_comment')
]