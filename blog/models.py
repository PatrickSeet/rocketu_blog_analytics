from django.db import models
from localflavor.us.models import USStateField


class Author(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()

    def __unicode__(self):
        return u"{}".format(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u"{}".format(self.name)


class Post(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __unicode__(self):
        return u"{}".format(self.title)


class Ads(models.Model):
    ad_url = models.URLField(unique=True)
    ad_name = models.CharField(max_length=50)
    ad_image = models.ImageField(upload_to="ad_image", blank=True)
    state = USStateField(null=True)

    def __unicode__(self):
        return u"{} {} {}".format(self.ad_name, self.ad_url, self.state)