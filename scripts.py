import os
import django
import itertools
os.environ['DJANGO_SETTINGS_MODULE']='firstproject.settings'
django.setup()
from home.models import Product
from django.db.models import Avg,Min,Max,Sum,Count,Q
from django.db.models.functions import ExtractYear
from django.db.models import OuterRef,Subquery
import requests

# url="https://dummyjson.com/products?limit=400"
# response = requests.get(url)
# data = response.json()

# for product_data in data['products']:
#     try:
#         product = Product(
#             title = product_data['title'],
#             description = product_data['description'],
#             category = product_data['category'],
#             price = product_data['price'],
#             brand = product_data['brand'],
#             sku = product_data['sku'],
#             thumbnail = product_data['thumbnail']
#         )
#         product.save()


#     except Exception as e:
#         print(e)


def querys():
    price=Product.objects.values('category').annotate(total=Avg('price'))


    for i in price:
        print(f"Name:{i['category']},Average:-{i['total']}")





querys()





