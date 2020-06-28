from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'home.html', {})


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
 