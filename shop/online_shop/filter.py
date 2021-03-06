import django_filters
from .models import Basket, Store, StoreType, Product

class BasketListFilter(django_filters.FilterSet):

    class Meta:
        model = Basket
        fields = {
            'status':['exact'],
            'created_on':['date__gt','date__lt'],
        }



class StoreListFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        fields = {
            'type':['exact',],
        } 

class StoreTypeFilter(django_filters.FilterSet):
    class Meta:
        model = StoreType
        fields = {
            'title':['exact','icontains'],
        }      

class ProductListFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'tag':['exact','icontains'],
            'price':['exact','lt', 'gt'],
            'stock':['exact','lt', 'gt'],
        }                 

        
           
          