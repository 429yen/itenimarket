from django_filters import filters
from django_filters import FilterSet
from .models import Product


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ProductFilter(FilterSet):

    name = filters.CharFilter(label = '商品名')

    order_by = MyOrderingFilter(
        fields = (
            ('name', 'name'),
        ),
        field_labels = {
            'name': '商品名'
        },
        label = '並び順'
    )


    class Meta:

        model = Product
        fields = ('name', 'type',)



