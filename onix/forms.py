# encoding: utf-8
from django.forms import TextInput, ModelForm, TextField

from onix.models import Block


class BlockForm(ModelForm):
    name = TextField(widget=TextInput(attrs={
        'placeholder': 'Digite o nome do material.',
    }))
    number = TextField(widget=TextInput(attrs={
        'placeholder': 'Digite o numero do bloco.',
    }))

    class Meta:
        model = Block
