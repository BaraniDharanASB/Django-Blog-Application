from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
import logging
from .models import Post, Category, Comment, ContactMessage
from .forms import contact_form, CommentForm

logger = logging.getLogger("TESTING")


def index(request):
    blog_title = "Latest posts"
    all_posts = Post.objects.all().order_by('-created_at')

    # Category filter
    category_id = request.GET.get('category', '').strip()
    if category_id:
        all_posts = all_posts.filter(category_id=category_id)

    # Search filter
    query = request.GET.get('q', '').strip()
    if query:
        all_posts = all_posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    categories = Category.objects.all()

    # Pagination
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {
        'blog_title': blog_title,
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    })


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    related_post = Post.objects.filter(category=post.category).exclude(pk=post.id) if post.category else Post.objects.exclude(pk=post.id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Your comment has been added successfully!")
            return redirect('blog:detail', slug=post.slug)
        else:
            messages.error(request, "Please check your comment details and try again.")
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'related_post': related_post,
        'comments': comments,
        'comment_form': comment_form,
    })


def about_view(request):
    return render(request, 'blog/about.html', {'blog_title': 'About Us'})


def contact_view(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            logger.debug(f'POST Data saved: {form.cleaned_data["name"]} {form.cleaned_data["email"]}')
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully.")
            return redirect('blog:contact')
        else:
            logger.debug('Form validation failure')
            messages.error(request, "Please correct the errors in the form below.")
            return render(request, 'blog/contact.html', {'form': form})
    else:
        form = contact_form()
        return render(request, 'blog/contact.html', {'form': form})


def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))


def new_url_view(request):
    return HttpResponse("this is the new link")
