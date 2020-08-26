from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save ,post_save,pre_delete
import pika
# Create your models here.

#to ayande inam hal ezafe mikonam  be zir daste ha felan dasti berim jolo
class credentials (models.Field):
    name = models.CharField(max_length=50,default="Counsumer 1")
    Broker_ip  = models.GenericIPAddressField(protocol="IPv4",default="127.0.0.1")
    port = models.SmallIntegerField(default=1884)
    username   = models.CharField(max_length=50,default="hgh")
    password   = models.CharField(max_length= 50,null=True,blank=True)

class CreateQueue (models.Model):
    name = models.CharField(max_length=50,default="Queue 1")
    
    Durable = models.BooleanField(default=True)
    exchange    =models.CharField(max_length= 100,default='ex.mqtt')
    Routing_Key =models.CharField(max_length= 100,null=True,blank=True)
    #use as QueueName
    slug =models.SlugField(null=True,blank=True)
    
    timestamp   = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.name
def create_queue(sender , instance , *args, **kwargs):
    credentials = pika.PlainCredentials('hgh', 'guest')
    parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel(1)
    channel.queue_declare(queue=instance.slug,durable=instance.Durable)
    if not instance.Routing_Key:
        channel.queue_bind(queue=instance.slug,exchange=instance.exchange)
    else:
        channel.queue_bind(queue=instance.slug,exchange=instance.exchange,routing_key=instance.Routing_Key)
    channel.close()
    connection.close()
post_save.connect(create_queue , sender=CreateQueue)

def delet_queue(sender , instance , *args, **kwargs):
    try:
        credentials = pika.PlainCredentials('hgh', 'guest')
        parameters = pika.ConnectionParameters('localhost',5672,'/',credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel(1)
        channel.queue_delete(instance.slug)
        channel.close()
        connection.close()
    except:
        havij=1
pre_delete.connect(delet_queue , sender=CreateQueue)


def save_QueueName(sender , instance , *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(save_QueueName , sender=CreateQueue)
    

class CreateConsumer (models.Model):
    name = models.CharField(max_length=50,default="Counsumer 1")
    Queue_Name = models.CharField(max_length=100,null=True,blank=True,default='queue-1')
    Pre_fetch = models.SmallIntegerField(default=2)
    Time_to_Consume = models.SmallIntegerField(default=1)
    #use as Consumer_Tag
    slug=models.SlugField(null=True,blank=True)
    

    timestamp   = models.DateTimeField( auto_now_add=True)
    last_update = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.name
        
def save_Consumer_Tag(sender , instance , *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(save_Consumer_Tag , sender=CreateConsumer)
