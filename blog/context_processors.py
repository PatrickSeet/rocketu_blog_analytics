from blog.models import Post, Tag, Ads

__author__ = 'Badmuthafucker'
def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }

def tags_posts(request):
    return {
        'tags_posts': Tag.objects.all()
    }

def ads(request):

    return {
        'ads': Ads.objects.all().order_by('?').first()
    }