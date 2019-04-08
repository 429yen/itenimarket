from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Product
from .filters import ProductFilter
from .forms import ProductForm


# Create your views here.
#検索一覧画面
class ProductFilterView(LoginRequiredMixin, FilterView):
    model = Product
    filterset_class = ProductFilter

    #デフォルトの並び順を新しいじゅんとする
    queryset = Product.objects.all().order_by('-created_at')

    # クエリ未指定の時に全件検索を行うために以下のオプションを設定
    strict = False

    #1ページあたりの表示件数
    paginate_by = 10

    #検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


#そうさい画面
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


#登録画面
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')


#更新画面
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')


#削除画面
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('index')