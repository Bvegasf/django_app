from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
    

urlpatterns = [
    
    path('',views.blog, name= "blog"),
    path('category/<category_id>', views.category, name="category")
]
