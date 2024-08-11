from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    data={}
    instance=Product.objects.all().order_by("?").first()
    if instance:
        data=ProductSerializer(instance).data

    return Response(data)    

    


