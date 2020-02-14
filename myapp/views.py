from django.shortcuts import render, get_object_or_404
from .models import Post, Post2
from django.contrib.auth.models import User
from my_django15_project.core.forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

me = User.objects.get(username='admin')


def post_list(request):
    get_all_data = Post.objects.all()
    get_all_post2_data = Post2.objects.all()
    get_data_by_id = Post.objects.filter(author=me)
    return render(request, 'blog/post_list.html', {'get_all_data': get_all_data, 'get_data_by_id': get_data_by_id,
                                                   'get_all_post2_data': get_all_post2_data})


def post_detail(request, pk):
    get_data_by_id = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'get_data_by_id': get_data_by_id})


# def post_new(request):
#
#     form = PostForm()
#     return render(request, 'blog/new_post.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = me
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post2, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = me
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    post_del = get_object_or_404(Post2, pk=pk)
    post_del.delete()
    return redirect('post_list')
