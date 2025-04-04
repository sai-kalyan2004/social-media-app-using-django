from django import forms
from .models import Post  # ✅ Import the Post model correctly

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
