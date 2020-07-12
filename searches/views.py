from django.shortcuts import render
from blog.models import BlogPost
from .models import SearchQuery

# Create your views here.

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    
    context = {"query":query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        #blog_list = BlogPost.objects.all().search(query=query) # Search all the blog post
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
        print("SEARCH")
    return render(request, 'search/view.html',context)
    