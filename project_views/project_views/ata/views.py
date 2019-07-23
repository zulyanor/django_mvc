from django.shortcuts import render
from .models import Mentee, Mentor, Blog
from .forms import MenteeForm, MentorForm, BlogForm
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    artikel = Blog.objects.all
    return render(request, 'blog.html', {'artikel':artikel})

def input_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = BlogForm()
    return render(request, 'bloginput.html', {'form':form})

def mentee(request):
    murid = Mentee.objects.all
    return render(request, 'mentee.html', {'murid':murid})

def input_mentee(request):
    if request.method == "POST":
        form = MenteeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = MenteeForm()
    return render(request, 'menteeinput.html', {'form':form})

def mentor(request):
    guru = Mentor.objects.all
    return render(request, 'mentor.html', {'guru':guru})

def input_mentor(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = MentorForm()
    return render(request, 'mentorinput.html', {'form':form})


def author(request):
    return render(request, 'author.html')

def blog_detail(request,blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'blog_detail.html', {'artikel':blog})
