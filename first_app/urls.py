
from django.urls import path
from .views import *

# app_name = AppName

urlpatterns = [
    path('', index, name='home'),
    path('get-in-touch/', contact_me, name='contact'),
    path('services/', services, name='services'),
    path('post-list', post_list, name='post_list'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('resume', resume, name='resume'),
    # path('post/<int:pk>/comment/', comment_create, name='comment_create'),
    # path('post/<int:pk>/reply/', reply_create, name='reply_create'),
    # path('create/', post_create, name='post_create'),
    # path('<int:pk>/update/', post_update, name='post_update'),
    # path('<int:pk>/delete/', post_delete, name='post_delete'),
    # path('list/', PostListView.as_view(), name='post_list_view'),
]