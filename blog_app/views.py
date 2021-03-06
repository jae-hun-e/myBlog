from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogFrom, BlogModelForm, CommentForm


def home(req):

    # posts = Blog.objects.all() # 블로그 모든 객체들 정보를 받아옴
    posts = Blog.objects.filter().order_by('-date') # 날짜를 기준으로 정렬된 데이터 가져옴 (-는 오름차순)
    return render(req, 'index.html', {'posts': posts})


# HTML Form을 이용해서 DB에 저장하기
# blog 글 작성
def new(req):
    return render(req, 'new.html')


# blog 글 저장
def create(req):
    if req.method == "POST":
        post = Blog()  # blog 객체 생성
        post.title = req.POST['title']
        post.body = req.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')  # 다시 돌아가라


# django form 으로 입력값을 받음 (GET, POST둘다 가능)
def form_create(req):
    # 입력값을 DB에 저장하는 로직
    if req.method == "POST":
        form = BlogFrom(req.POST)
        if form.is_valid():
            post = Blog()
            post.title = req.POST['title']
            post.body = req.POST['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    # 입력값을 받을 수있는 html을 갖다 줌
    else:
        form = BlogFrom()
    return render(req, 'form_create.html', {'form': form})  # 세번째 인자는 views.py내의 데이터를 html로 넘겨줄 수 있음 단, 딕셔너리 자료형이여야함)


# model form으로 입력값을 받음
def modelformcreate(req):
    # 입력값을 DB에 저장하는 로직
    if req.method == "POST" or req.method == "FILES":
        form = BlogModelForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    # 입력값을 받을 수있는 html을 갖다 줌
    else:
        form = BlogModelForm()
    return render(req, 'form_create.html', {'form': form})  # 세번째 인자는 views.py내의 데이터를 html로 넘겨줄 수 있음 단, 딕셔너리 자료형이여야함)


# detail page
def detail(req, blog_id):
    # blog_id번째 블로그 글을 DB에서 가져옴
    blog_detail = get_object_or_404(Blog, pk=blog_id)  # 못가져오면 404 띄워라

    comment_form = CommentForm()  # CommentForm객체 가져옴

    return render(req, 'detail.html', {'blog_detail' : blog_detail, 'comment_form' : comment_form})

# create comment
def create_comment(req, blog_id):
    filled_form = CommentForm(req.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)