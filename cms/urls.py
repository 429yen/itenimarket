from django.urls import path
from .views import ProductFilterView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    #一覧画面
    path('', ProductFilterView.as_view(), name='index'),
    #そうさい画面
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    #登録画面
    path('create/', ProductCreateView.as_view(), name='create'),
    #更新画面
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    #削除画面
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]

