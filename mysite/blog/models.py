from .managers import *
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# import choices vars
from .choices import STATUS_CHOICES


# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
    unique_for_date='publish')
    author = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
    choices=STATUS_CHOICES,
    default='draft')

    objects = models.Manager() 
    published = PublishedManager() 
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day, self.slug])