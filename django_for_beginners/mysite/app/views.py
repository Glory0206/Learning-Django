from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView
from app.models import Post
from app.forms import PostForm

# Create your views here.
def index(request: HttpRequest) -> HttpRequest:
    qs = Post.objects.all()

    return render(request, "app/index.html", {"post_list": qs})

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)

    return render(request, "app/post_detail.html", {"post": post})

post_new = CreateView.as_view(
    model = Post,
    form_class = PostForm,
    success_url="/app/",
)