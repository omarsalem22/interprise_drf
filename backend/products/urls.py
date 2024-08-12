from django.urls import path
from.views import ProductDetailApiView,ProductCreateApoView,ProductListCreateApiView,product_alt_view,ProductUpdateApi,ProductDeleteApi


urlpatterns = [
    path("<int:pk>/",ProductDetailApiView.as_view()),
    path("create/",ProductCreateApoView.as_view()),
    path("listcreate/",ProductListCreateApiView.as_view()),

    path("product_alt/",product_alt_view),

    path("product_alt/<int:pk>",product_alt_view),

    path("update/<int:pk>",ProductUpdateApi.as_view()),

    path("delete/<int:pk>",ProductDeleteApi.as_view()),
    

  


    


]
