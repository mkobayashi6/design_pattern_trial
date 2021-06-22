from django.shortcuts import render

from .models import Category
from .myFunction import IdnameIterator

# Create your views here.
def index(request):
    latest_category_list = Category.objects.order_by('-pub_date')[:5]
    categories = []
    for category in latest_category_list:
        categories.append({category.id, category.name})
    contents = IdnameIterator.IdnameIterator(categories)
    context = {'latest_category_list': contents}
    return render(request, 'iterator_trial/index.html', context)

def detail(request, category_id):
    context = {
        'category_id': category_id,
    }
    return render(request, 'iterator_trial/detail.html', context)