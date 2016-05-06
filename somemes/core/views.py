from django.shortcuts import render
from somemes.core.models import Meme


def home(request):
    context = {'memes': Meme.list_all()}
    return render(request, 'index.html', context=context)
