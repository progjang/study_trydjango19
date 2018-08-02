from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from datetime import timezone, datetime
from django.db.models import Q
# Create your views here.

def posts_home(request):
    queryset = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
            ).distinct()

    paginator = Paginator(queryset, 5) # Show 3 posts per page

    page = request.GET.get('page')
    try:
        instances = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        instances = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        instances = paginator.page(paginator.num_pages)

    return render(request, 'posts/post_list.html', {'instances': instances})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Successfully Created")
            #return redirect("posts:detail", id=post.id)
            return redirect(post)
        else:
            messages.error(request, "Not Successfully Created")
    else:
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "posts/post_form.html", context)

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        'instance' : instance,
    }
    return render(request, 'posts/post_detail.html', context)

def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Item Saved")
            #return redirect("posts:detail", id=post.id)
            return redirect(post)
        else:
            messages.error(request, "Not Successfully Saved")
    else:
        form = PostForm(instance=instance)

    context = {
        "form": form,
    }
    return render(request, "posts/post_form.html", context)

def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Item deleted.")
    return redirect("posts:posts_home")

    
