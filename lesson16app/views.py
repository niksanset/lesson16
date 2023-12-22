from django.shortcuts import render

from lesson16app.models import Post


def post_list_view(request):

    context = {'post_list': Post.objects.all()}

    return render(request,
                  'lesson16app/post_list.html',
                  context)


def post_create_view(request):
    return render(request,
                  'lesson16app/post_create.html')


