
from django.urls import path
from shoppin_kart import views
from django.conf import settings
from django.conf.urls.static import static
from shoppin_kart.views import add, delette, rest, clean
    
app_name = "shopping"
urlpatterns = [
    path("add/<int:product_id>/", views.add , name="agregar"),
    path("delete/<int:product_id>/", views.delette , name="eliminar"),
    path("rest/<int:product_id>/", views.rest , name="restar"),
    path("clean/<int:product_id>/", views.clean , name="limpiar"),
    
]
