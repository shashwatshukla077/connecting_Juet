
from django.contrib import admin
from django.urls import path , include
from user import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cjuet/',include('main.urls')),
    path('register/',user_views.register,name='register')
]
