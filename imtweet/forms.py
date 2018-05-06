from django.contrib.auth.models import User
from .models import Post, Comment
from django import forms

class UserList(forms.Form):
    list=[]
    for e in User.objects.all():
        list.append((e.username,e.username))
    field = forms.ChoiceField(choices=list)

# class Search(forms.Form):
#     field = forms.CharField(max_length=150), label='')

class PostForm(forms.ModelForm):
    post_text = forms.CharField(max_length=140, widget=forms.Textarea(attrs={'rows':4, 'cols':35}), label='')
    class Meta:
        model = Post
        fields = ('post_text',)

class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=140, widget=forms.Textarea(attrs={'rows':4, 'cols':35}), label='')
    class Meta:
        model = Comment
        fields = ('comment_text',)
