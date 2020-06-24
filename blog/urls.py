from django.urls import path, include
from . import views

urlpatterns = [
    #path('',views.blog_post_detail, name='BlogPost'),
    path('<str:slug>/', views.blog_post_detail, name='BlogPost2'),
    #path(r'^blog/(?P<post_id>\d+)/$', include('blog.urls')),
    
]