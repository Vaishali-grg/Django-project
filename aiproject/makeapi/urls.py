from django.urls import path
from . import views
urlpatterns=[
    path('',views.get_products_view,name="products"),
    path('<int:id>',views.get_single_product,name="product"),
]