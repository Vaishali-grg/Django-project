from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# @api_view(["GET","POST"])
@api_view()#product view will convert product into 

def get_products_view(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data,status=200) #JSON (java script object notation)Object

@api_view()
def get_single_product(request,id):
    return Response(f"SIngle Product {id}")
