from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    content = RichTextField()
    #content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    #reactions = models.ManyToManyField(User, related_name='blog-posts', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #comment = models.TextField()
    comment = RichTextField()
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True,blank = True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + ': ' + self.comment[:10]
    '''
        def get_absolute_url(self):
            return reverse('post-detail', kwargs={'pk': self.pk})
    '''