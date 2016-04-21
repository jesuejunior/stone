# encoding: utf-8
from django.forms import TextInput, ModelForm, ChoiceField

from onix.models import Question


class QuestionForm(ModelForm):
    answer = ChoiceField(widget=TextInput(attrs={
        'placeholder': 'Marque a resposta correta.',
    }))

    class Meta:
        model = Question
