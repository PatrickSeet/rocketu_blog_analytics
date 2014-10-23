from django.shortcuts import render, get_object_or_404
from analytics.models import Page, View
from blog.models import Post


# def home(request):
#     return render(request, 'home.html', {
#         'latest_post': Post.objects.latest('created')
#         # same as:
#         # 'latest_post': Post.objects.order_by('-created')[0]
#     })

def main(request):
    return render(request, 'main.html', {
        'pages': Page.objects.all(), 'page': View.objects.order_by().values('page_id').distinct()
    })

def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })

def postwithtags(request, id):

    posts = Post.objects.filter(tags=id)

    return render(request, 'post_tag.html', {
        'posts': posts
    })
def post(request, pk):

    # try:
    #     post_obj = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     pass
    # this will get 500 page, handel gracefully below

    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })

def error(request):
    my_variable = '!'
    my_list = ['testing', 'a', 'list', 'out']
    my_list = ["{}{}".format(list_item, my_variable) for list_item in my_list]
    raise NotImplementedError("Woops! This doesn't exist.")