from django.urls import path, include
from . import views

urlpatterns = [
    #Routing to blog app
    path('', views.blog_post_list_view),
    path('<str:slug>/', views.blog_post_detail_view), # The back-slash at the back is important to stay on the page after operations
    path('<str:slug>/edit/', views.blog_post_update_view),
    path('<str:slug>/delete/', views.blog_post_delete_view),

]