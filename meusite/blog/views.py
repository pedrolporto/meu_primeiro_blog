from django.shortcuts import render

# Create your views here.

def listar_post(request):
    return render(request, 'blog/listar_post.html', {})