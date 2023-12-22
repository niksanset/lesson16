from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,)
    audio = models.FileField(upload_to='audio/',
                             null=True,
                             blank=True,)
    video = models.FileField(upload_to='video/',
                             null=True,
                             blank=True,)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
