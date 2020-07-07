from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost

def home(request):
    qs = BlogPost.objects.all()[:5] # Only select first 5 posts
    context = {
        'title': "Welcome to Shadow's Site",
        'blog_list': qs,
    }
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html', {})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid(): # if form is valid with correct fields
        print(form.cleaned_data) # clean the data to be disctionary format
        form = ContactForm() # This will clear the form
    context = {
        'title': 'Contact Us',
        'form': form,
    }
    return render(request, 'form.html', context)
 