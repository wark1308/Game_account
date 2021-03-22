from django.db import models
from django.utils import timezone
from user_req.models import User


class Topper(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    topper_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    info = models.TextField(null=True)
    money = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
 
    class Meta:
        verbose_name = 'topper'
        verbose_name_plural = 'topper'

    def __str__(self):
        return self.topper_name


class Advertisement(models.Model):
    
    topper = models.ForeignKey(Topper, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} - by {self.post}'


class AdverImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ad_image')
    description = models.CharField(max_length=55)

    def __str__(self):
        if self.image:
            return self.image.url
        return ''


class Commentary(models.Model):
    topper = models.ForeignKey(Topper, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    