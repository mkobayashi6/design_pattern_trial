from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Category, SubCategory
from .myFunction import IdnameIterator

# Create your views here.
def index(request):
    latest_category_list = Category.objects.order_by('-pub_date')[:5]
    categories = []
    for category in latest_category_list:
        categories.append({category.id, category.name})
    contents = IdnameIterator.IdnameIterator(categories)
    return render(request, 'iterator_trial/index.html', {'latest_category_list': contents})

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'iterator_trial/detail.html', {'category': category, 'choices': SubCategory.Gender.choices})

def gender(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategory = get_object_or_404(SubCategory, pk=request.POST['sub_id'])
    gender = int(request.POST[str(subcategory.id)+'_choice'])
    if gender in SubCategory.Gender.values:
        subcategory.gender = gender
        subcategory.save()
        return HttpResponseRedirect(reverse('iterator_trial:results', args=(subcategory.id,)))
    else:
        return render(request, 'iterator_trial/detail.html', {
                'category': category,
                'choices': SubCategory.Gender.choices,
                'error_message': "Invalid gender choised",
        })

def results(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, pk=subcategory_id)
    return render(request, 'iterator_trial/results.html', {'subcategory': subcategory, 'gender': SubCategory.Gender(subcategory.gender).label})