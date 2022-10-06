from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    postlar = Post.objects.all()
    return render(request, 'home.html', {'postlar':postlar})


def error_view(request, exception):
    return render(request, 'error.html')