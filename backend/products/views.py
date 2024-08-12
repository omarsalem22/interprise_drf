from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'


class ProductCreateApoView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)

class ProductListCreateApiView(generics.ListCreateAPIView):

       queryset=Product.objects.all()
       serializer_class=ProductSerializer

       def perform_create(self,serializer):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)




@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args, **kwargs):
     method=request.method
     if request.method=="GET":
          if pk is not None:
               #detail
               obj=get_object_or_404(Product,pk=pk)
               data=ProductSerializer(obj,many=False).data

               return Response(data)
          
          #list
          queryset=Product.objects.all()
          data=ProductSerializer(queryset,many=True).data

          return Response(data)
     

     if request.method=="POST":
          
          #createitem
          
          serializer=ProductSerializer(data=request.data)

          if serializer.is_valid(raise_exception=True):
               
               title=serializer.validated_data.get("title")
               content=serializer.validated_data.get('content') or None
               if content is None:
                    content=title
               serializer.save()
               return Response(serializer.data) 
          return Response({"invalid":"not good data"},status=400)

class ProductUpdateApi(generics.UpdateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer 
     lookup_field='pk'

     def Perform_update(self,serializer):
          
          instance=serializer.save()

          if not instance.content:
               instance.content=instance.title




class ProductDeleteApi(generics.DestroyAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer 
     lookup_field='pk'

     def perform_destroy( instance):
          return super().perform_destroy(instance)
     









          
   


          