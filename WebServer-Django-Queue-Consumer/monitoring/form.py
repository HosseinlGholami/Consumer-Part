from django import forms

from .models import CreateQueue,CreateConsumer


class QueueCreatForm (forms.ModelForm):
    class Meta:
        model  = CreateQueue
        fields = [    
            "name",
            "Durable",
            "exchange",
            "Routing_Key",
        ]


class ConsumerCreatForm (forms.ModelForm):
    class Meta:
        model  = CreateConsumer
        fields = [
                "name",
                "Queue_Name",
                "Pre_fetch",
                "Time_to_Consume",
        ]
























class ConsumerCreatFormClassic(forms.Form):
    name              = forms.CharField(initial='Consumer')
    Broker_ip         = forms.GenericIPAddressField(protocol="IPv4",initial='127.0.0.1')
    port              = forms.IntegerField(widget=forms.HiddenInput(), initial=1884)
    username          = forms.CharField(required=False)
    password          = forms.CharField(required=False)
    Queue_Name        = forms.CharField(required=False)
    packet_to_consume = forms.IntegerField()
