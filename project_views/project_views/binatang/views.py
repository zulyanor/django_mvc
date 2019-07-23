from django.shortcuts import render
from .models import Hewan
from .forms import InputHewan

# Create your views here.
def daftar_binatang(request):
    return render(request, 'binatang.html')

def db_binatang(request):
    binatang = Hewan.objects.all
    return render(request, 'binatang.html', {'binatang' : binatang})

def input_Hewan(request):
    if request.method == "POST":
        form = InputHewan(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = InputHewan()
    return render(request, 'binatang.html', {'form':form})