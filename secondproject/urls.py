
from django.contrib import admin
from django.urls import path
import blog.views
from django.urls import include, path
from .views import UserCreateView
from django.conf import settings
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name= "home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name="create"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]
