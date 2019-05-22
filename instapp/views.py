from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image
from django.utils import timezone


# Create your views here.

# def home(request):
#     return render(request, 'instapp/home.html')

def home(request):
    return render(request, 'instapp/home.html')


@login_required
def post(request):
    if request.method == 'POST':
        if request.FILES['post_image'] and request.POST['image_name'] and request.POST['image_caption']:
            image = Image()
            image.post_image = request.FILES['post_image']
            image.image_name = request.POST['image_name']
            image.image_caption = request.POST['image_caption']
            image.pub_date = timezone.datetime.now()
            image.user_profile = request.user
            image.save()
            return redirect('home')
        else:
            return render(request, 'instapp/post.html', {'error': 'All fields are required'})
    else:
        return render(request, 'instapp/post.html')
