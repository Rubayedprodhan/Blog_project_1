from django.shortcuts import render,redirect
from . import models
from . import froms
# Create your views here.
def add_Post(request):
    if request.method== 'POST':
        post_form=froms.PostFrom(request.POST)
        if post_form.is_valid():
            post_form.save()
        
            return redirect('add_post')
    else:
        post_form=froms.PostFrom()
    return render (request, 'add_post.html',{'from':post_form})



def edit_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post_form = froms.PostFrom(instance=post)

    # print(post.title)
    if request.method == 'POST':
        post_form = froms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
             
            post_form.save() 
            return redirect('homepage')
    
    return render(request, 'add_post.html', {'from' : post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
