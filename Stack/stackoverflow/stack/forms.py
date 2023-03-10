from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","fullname","email","phone","address","image"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['name','tag','description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['ans']