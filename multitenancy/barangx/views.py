from django.shortcuts import render
from .models import Post


def home(request):
    barang = Post.objects.all()
    return render(request, 'home.html', {'barang': barang})
