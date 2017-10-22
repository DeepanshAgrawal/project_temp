from django import forms
from .models import *

class FeedbackForm(forms.ModelForm):
    suggestions = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Feedback
        fields = ['name', 'suggestions']
class MusicForm(forms.ModelForm):
    class Meta:
        model=music
        fields = ['name','songs_name','songs_singer','category']

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields = ['name','movie_name','movie_director','category']