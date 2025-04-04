from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Like
from .forms import PostForm


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the logged-in user
            post.save()
            return redirect('home')  # Redirect to home page or post list
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_list(request):
    posts = Post.objects.prefetch_related("likes").order_by("-created_at")

    for post in posts:
        post.is_liked = post.likes.filter(user=request.user).exists()  # Mark whether the user liked this post

    return render(request, "posts/post_list.html", {"posts": posts})


@csrf_exempt  # Optional: Only if CSRF issues persist
@login_required
def like_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:  # If like already exists, remove it (unlike)
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({"liked": liked, "likes_count": post.likes.count()})

    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)  # Ensure user owns the post
    post.delete()
    return redirect('profile')
