from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPostModel
from django.core.paginator import Paginator



class BlogListView(ListView):
    template_name = 'main/blog.html'
    model = BlogPostModel
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        blog = super(BlogListView, self).get_queryset(*args, **kwargs)
        blog = blog.order_by('-id')
        return blog

class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog-details.html'
    context_object_name = 'post'
    paginate_by = 2


    # def Paginator(request):
    #     p = Paginator(BlogPostModel.objects.all(), 2)
    #     page = request.GET.get('page')
    #     blogs = p.get_page(page)
    #
    #     return render(request, 'main/blog-details.html', context={
    #         'blog_list' :
    #     })



def listing(request):
    contact_list = BlogPostModel.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})