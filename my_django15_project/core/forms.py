from django import forms

from my_django15_project.core.models import PostGroup2


class PostForm(forms.ModelForm):

    class Meta:
        model = PostGroup2
        fields = ('title', 'text',)
