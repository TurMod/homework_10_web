from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, Textarea
from django.db import models
from .models import Author, Quote


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    biography = Textarea()

    class Meta:
        model = Author
        fields = ['fullname', 'biography']


class QuoteForm(ModelForm):

    quote = Textarea()

    # choices = []
    #
    # for i, author in enumerate(Author.objects.all()):
    #     choices.append((author, author))

    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
