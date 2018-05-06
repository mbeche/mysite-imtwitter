from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=140)
    pud_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_text

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment_text
# Create your models here.
