from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PostGroup, PostGroup2
from my_django15_project.core.forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'user_count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
         'form': form
     })


me = User.objects.get(username='admin')
# user = User.objects.get(username=user.username)


@login_required
def post_list(request):
    get_all_data = PostGroup.objects.all()
    queryset = PostGroup2.objects.select_related('author').all()
    # post_with_user = []
    # breakpoint()
    # for post_with_user in queryset:
    #     print({'id': post_with_user.id,
    #            'author_id': post_with_user.author_id,
    #            'title': post_with_user.title,
    #            'text': post_with_user.text,
    #            'created_date': post_with_user.created_date,
    #            'published_date': post_with_user.published_date,
    #            'author_name': post_with_user.author.username
    #            })

    get_data_by_id = PostGroup.objects.filter(author=me)
    return render(request, 'blog/post_list.html', {'get_all_data': get_all_data, 'get_data_by_id': get_data_by_id,
                                                   'get_all_post2_data': queryset})


@login_required
def post_detail(request, pk):
    get_data_by_id = get_object_or_404(PostGroup, pk=pk)
    return render(request, 'blog/post_detail.html', {'get_data_by_id': get_data_by_id})


# def post_new(request):
#
#     form = PostForm()
#     return render(request, 'blog/new_post.html', {'form': form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(PostGroup2, pk=pk)
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


@login_required
def post_delete(request, pk):
    post_del = get_object_or_404(PostGroup2, pk=pk)
    post_del.delete()
    return redirect('post_list')
