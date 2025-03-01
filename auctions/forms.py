from django import forms
from django.forms import ModelForm
from .models import Listing, Bids, Comment


# Create a form 
class NewForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'starting_bid', 'image_url','category')
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 450px;'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'style':'width: 450px;'}),
            "starting_bid": forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 450px;'}),
            "image_url": forms.TextInput(attrs={'class': 'form-control','style': 'width:450px;'}),
            "category": forms.Select(attrs={'class': 'form-control','style': 'width: 450px;' }),

        }

class BidForm(ModelForm):
    class Meta:
         model = Bids
         fields =('current_bid',)
         labels = {
            "current_bid": ("")
            }
         widgets ={
         'current_bid': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 450px;'}) 
      }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": ("")
            }
        widgets = {
            "comment": forms.Textarea(attrs={
                "placeholder": "Add your comment here",
                "class": "form-control",
                "rows": 1
            })
        }



