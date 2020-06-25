from django.shortcuts import render, get_object_or_404 
from django.http import Http404

# Create your views here.
from .models import BlogPost


def blog_post_list_view(request):
    # List out objects
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = { "object_list": qs }
    return render(request, template_name, context)
    
def blog_post_create_view(request):
    # create objects by using a form
    template_name = 'blog/create.html'
    context = { "form": '' }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detailed view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = { "object": obj} 
    return render(request, template_name, context)

def blog_post_update_view(request,slug):
    # update objects by using a form
    #obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = { "object_list": [], "form": '' }
    return render(request, template_name, context)

def blog_post_delete_view(request,slug):
    # delete objects by using a form
    #obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = { "form": '' }
    return render(request, template_name, context)
