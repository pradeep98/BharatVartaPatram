from django import forms
from django.contrib.auth.models import User
from .models import PostComment



class CreatePostComment(forms.ModelForm):
    class Meta:
        model = PostComment
        #fields = ['comment']

        #widget = {'parent': forms.HiddenInput}
        fields = ['comment','parent']
        widgets={'parent': forms.HiddenInput()}

    '''
    def __init__(self, *args, **kwargs):
        super(CreatePostComment, self).__init__(*args, **kwargs)
        self.fields['parent'].required = False
    '''   
    
    