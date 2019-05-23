from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    post_image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)
    image_caption = models.TextField()
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.TextField()

    def __str__(self):
        return self.image_name

    def pub_date_format(self):
        return self.pub_date.strftime('%b %e %Y')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)
    prof_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.user.username} Profile'
