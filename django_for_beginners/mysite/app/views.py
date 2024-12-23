from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.models import Post

# Create your views here.
def index(request: HttpRequest) -> HttpRequest:
    qs = Post.objects.all()

    return render(request, "index.html", {"post_list": qs})