from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


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

