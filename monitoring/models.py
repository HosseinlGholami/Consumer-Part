from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.
class Consumer (models.Model):
    name = models.CharField(max_length=50,default="Counsumer 1")
    Broker_ip  = models.GenericIPAddressField(protocol="IPv4",default="127.0.0.1")
    port = models.SmallIntegerField(default=1884)
    username   = models.CharField(max_length=50,default="hgh")
    password   = models.CharField(max_length= 50,null=True,blank=True)
    Queue_Name = models.CharField(max_length=100,null=True,blank=True)
    packet_to_consume = models.SmallIntegerField(null=True,blank=True)

    timestamp   = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField( auto_now=True)

    slug        = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
        
def save_slug(sender , instance , *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(save_slug , sender=Consumer)
