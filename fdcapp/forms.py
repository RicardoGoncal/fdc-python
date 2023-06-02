from django import forms
from fdcapp.models import PostRequestCloud

class FormRequestCloud(forms.ModelForm):
    
    class Meta():
        model = PostRequestCloud
        fields = ('solicitante',)

        widgets = {
            'solicitante': forms.TextInput(attrs={'class': 'textinputclass'}),
        }


class FormRequestNetwork(forms.ModelForm):
    pass