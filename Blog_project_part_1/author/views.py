from django.shortcuts import render,redirect
from . import froms
# Create your views here.

def add_author(request):
    if request.method== 'POST':
        authorFroms=froms.AuthorFrom(request.POST)
        if authorFroms.is_valid():
            authorFroms.save()
        
            return redirect(add_author)
    else:
        authorFroms=froms.AuthorFrom()
    return render (request, 'add_author.html',{'from':authorFroms})

