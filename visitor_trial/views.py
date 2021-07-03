from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'visitor_trial/index.html', context)

def detail(request, category_id):
    context = {}
    return render(request, 'visitor_trial/detail.html', context)