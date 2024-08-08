from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone  # Add this line to import the timezone module
from .models import Post, Like, Dislike
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'is_liked': post.likes.filter(user=request.user).exists(),
        'is_disliked': post.dislikes.filter(user=request.user).exists(),
    })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.dislikes.filter(user=request.user).exists():
        post.dislikes.filter(user=request.user).delete()
    if not post.likes.filter(user=request.user).exists():
        Like.objects.create(user=request.user, post=post)
    return redirect('post_detail', post_id=post.id)


def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(user=request.user).exists():
        post.likes.filter(user=request.user).delete()
    if not post.dislikes.filter(user=request.user).exists():
        Dislike.objects.create(user=request.user, post=post)
    return redirect('post_detail', post_id=post.id)
