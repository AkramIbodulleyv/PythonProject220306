from django.forms import ModelForm
from django import forms

from .models import Books, Category, Reviews


class ReviewCreateForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating', 'text')

