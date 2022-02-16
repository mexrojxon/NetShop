from pyexpat import model

from django.forms.models import ModelForm
from .models import CommentModel

class CommentModelForm(ModelForm):
    class Meta:
        model = CommentModel
        exclude =['post', 'created_at']