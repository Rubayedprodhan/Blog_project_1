from django.shortcuts import render,redirect
from . import froms
# Create your views here.
def add_Categories(request):
    if request.method== 'POST':
        Categories_From=froms.CategoriesFrom(request.POST)
        if Categories_From.is_valid():
            Categories_From.save()
        
            return redirect('Categories_From')
    else:
        Categories_From=froms.CategoriesFrom()
    return render (request, 'add_category.html',{'from':Categories_From})