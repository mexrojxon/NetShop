from pyexpat import model

import kwargs as kwargs
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentModelForm
from .models import BlogPostModel, CommentModel
from .forms import CommentModelForm



class BlogListView(ListView):
    template_name = 'main/blog.html'
    queryset = BlogPostModel.objects.order_by('-pk')
    model = BlogPostModel
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        qs = BlogPostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            return qs.filter(tags__title=tag)
        return qs

class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog-details.html'
    context_object_name = 'post'


class BlogCommentView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(BlogPostModel, pk=self.kwargs.get('pk'))
        return super(BlogCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs.get('pk')})