from django.shortcuts import render
from post.models import Post
def home(request):
    data= Post.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.Categories.all():
    #         print(j)
    #     print()
    return render (request, 'home.html', {'data' : data})
