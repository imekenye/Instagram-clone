from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Image,UserProfile
from django.utils import timezone


# Create your views here.

# def home(request):
#     return render(request, 'instapp/home.html')

def home(request):
    images = Image.objects.all()
    return render(request, 'instapp/home.html', {'images': images})


# def home(request, image_id):
#     images = get_object_or_404(Image, image_id)
#     return render(request, 'instapp/home.html', {'images': images})


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
            return redirect('/instapp/' + str(image.id))
        else:
            return render(request, 'instapp/post.html', {'error': 'All fields are required'})
    else:
        return render(request, 'instapp/post.html')


def imagedetail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'instapp/imagedetail.html', {'image': image})


def like(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(Image, pk=image_id)
        image.likes += 1
        image.save()
        return redirect('/instapp/' + str(image.id))
