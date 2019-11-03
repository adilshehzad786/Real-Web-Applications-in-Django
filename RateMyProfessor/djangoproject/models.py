from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    instructor=models.CharField(max_length=100)
    rating=models.IntegerField()
    comments=models.TextField()
    institute=models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    instructor_image=models.ImageField(default = 'default.jpg', upload_to = 'instructor_images/' )
    def __str__(self):
        return self.instructor

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





