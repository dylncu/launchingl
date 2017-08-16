from django.db import models
from django.utils import timezone
# Create your models here.
class Type(models.Model):
    posttype = models.CharField(max_length = 40)
    def __str__(self):
        return self.posttype
    def latestimage(self):
        obj = self.posts.latest("id")
        img = obj.images.latest("id")
        return img
    def latestimages(self):
        obj = self.posts.latest("id")
        imgs = obj.images.all()
        return imgs

class Post(models.Model):
    ptype = models.ForeignKey('blog.Type', related_name='posts')
    title = models.CharField(max_length = 100)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey('blog.Post', related_name='images')
    image = models.ImageField(upload_to='launchingl/', blank='true')

    def __str__(self):
        return self.image.name
