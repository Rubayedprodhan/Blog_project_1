from django.shortcuts import render,redirect

from . import froms
# Create your views here.
def add_profiles(request):
    if request.method== 'POST':
        Profile_From=froms.ProfileFrom(request.POST)
        if Profile_From.is_valid():
            Profile_From.save()
        
            return redirect(Profile_From)
    else:
        Profile_From=froms.ProfileFrom()
    return render (request, 'add_author.html',{'from':Profile_From})