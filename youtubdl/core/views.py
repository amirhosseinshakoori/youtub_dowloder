import pytube
from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponseRedirect
from . forms import SaveUrloathform


def index(request):
    return render (request, 'core/index.html')


def downloadLink(request):
    if request.method == 'POST':
        form=SaveUrloathform(request.Post)
        if form.is_valid():
            link= form.cleaned_data['link']
            if link:
                yt=pytube.YouTube(link)
                yt.streams.first.download()
                return HttpResponseRedirect('/')
    else:
        form = SaveUrloathform()
    return render(request,'core/new_download.html',{'form':form})    