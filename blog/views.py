from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm


def blog_post_list_view(request):
    # List out objects
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user = request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    context = { "object_list": qs }
    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    # create objects by using a form
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form.save()
        #obj = BlogPost.objects.create(**form.cleaned_data) 
        # A Django combined method. Saves the data to the database
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = { 
        "form": form,
        'title' : 'Create',
    }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detailed view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = { "object": obj} 
    return render(request, template_name, context)

def blog_post_update_view(request,slug):
    # update objects by using a form
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        print("saved form")
    template_name = 'form.html'
    context = {
        'form': form, 
        'title' : f'Update {obj.title}',
    }
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request,slug):
    # delete objects by using a form
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        print("Deleted: " + obj.title)
        return redirect("/blog") 
    template_name = 'blog/delete.html'
    context = { "object": obj }
    return render(request, template_name, context)
