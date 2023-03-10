from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import loader
from .forms import *

# Create your views here.
def index(request):

    services = Service.objects.all()[:6]
    context = {
        'form': ContactMeForm(),
        'services': services,
    }
    return render(request, 'my_app/index.html', context)

def contact_me(request):
  if request.method == "POST":
        form = ContactMeForm(request.POST)
        if form.is_valid():
              form.save()
              return redirect('home')
        return redirect('contact')
  
  else:
        form = ContactMeForm()

  return render(request, 'my_app/contact.html', {'form': form})


def services(request):
   return render(request, 'my_app/service.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'my_app/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    comments = post.comments.filter(parent_comment=None)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    categories = Category.objects.all()
    posts = Post.objects.all()[:3]

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                post.comment_count += 1
                post.save()
                return redirect('post_detail', id=id)

        elif 'reply_submit' in request.POST:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                parent_comment_id = request.POST.get('parent_comment')
                parent_comment = Comment.objects.get(pk=parent_comment_id)
                reply = reply_form.save(commit=False)
                reply.post = post
                reply.parent_comment = parent_comment
                reply.save()
                post.comment_count += 1
                post.save()
                return redirect('post_detail', id=id)

    # Increase view count on every GET request
    post.view_count += 1
    post.save()

    context = {
    'post': post,
    'comments': comments,
    'comment_form': comment_form,
    'reply_form': reply_form,
    'categories': categories,
    'posts': posts,
    }

    return render(request, 'my_app/post_detail.html', context)



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            post.increment_comment_count()
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increment_like_count()
    return render(request, 'post_detail.html', {'post': post})


def resume(request):
    return render(request, 'my_app/resume.html')