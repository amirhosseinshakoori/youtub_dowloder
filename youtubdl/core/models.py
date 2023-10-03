from collections.abc import Iterable
from django.db import models
import pytube
from pytube import YouTube


class SaveUrloath(models.Model):
    link = models.URLField(verbose_name='Youtub link')
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.link)
    
    def save(self,*args, **kwargs) :
        if not self.id:
            yt = pytube.YouTube(str(self.link))
            yt.streams.first().downloawd()
        return super(SaveUrloath,self).save(*args,**kwargs)