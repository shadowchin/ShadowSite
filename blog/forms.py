from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget = forms.Textarea)

# Model Forms from Django
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','slug', 'image','content', 'publish_date')

    def clean_title(self, *args, **kwargs):
        #print(dir(self)) # print out all the form details, we want to fing the "intsnace"
        instance = self.instance
        #print("INSTANCE: " + instance)
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact = title)
        if instance is not None: # Check if the instamce exist, 
            qs = qs.exclude(pk=instance.pk) # then exclude it from the next check....used for updating
        if qs.exists():
            print('Raised validation error')
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title