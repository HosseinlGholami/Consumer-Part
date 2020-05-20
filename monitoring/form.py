from django import forms

from .models import Consumer


class ConsumerCreatForm (forms.ModelForm):
    class Meta:
        model  = Consumer
        fields = [
            "name",
            "Broker_ip",
            "port",
            "username",
            "password",
            "Queue_Name",
            "packet_to_consume"
        ]


class ConsumerCreatFormClassic(forms.Form):
    name              = forms.CharField(initial='Consumer')
    Broker_ip         = forms.GenericIPAddressField(protocol="IPv4",initial='127.0.0.1')
    port              = forms.IntegerField(widget=forms.HiddenInput(), initial=1884)
    username          = forms.CharField(required=False)
    password          = forms.CharField(required=False)
    Queue_Name        = forms.CharField(required=False)
    packet_to_consume = forms.IntegerField()
