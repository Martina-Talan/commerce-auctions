from django import forms
from django.forms import ModelForm
from .models import Listing, Bids, Comment


# Create a form 
from django import forms
from django.forms import ModelForm
from .models import Listing

class NewForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'starting_bid', 'image_url', 'category')
        widgets = {
            "title": forms.TextInput(attrs={
               'placeholder': 'Enter title',
               'style': 'width: 430px; max-width: 500px; outline:none;',
            }),
            "description": forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Enter description',
                'style': 'width: 430px; max-width:  500px; outline:none;',
            }),
            "starting_bid": forms.NumberInput(attrs={
                'placeholder': 'Enter starting bid',
                'style': 'width: 430px; max-width:    500px; padding: 15px !important; outline:none;',
            }),
            "image_url": forms.TextInput(attrs={
                'placeholder': 'Enter image URL',
                'style': 'width: 430px; max-width: 500px; outline:none;',
            }),
            "category": forms.Select(attrs={
                'placeholder': 'Choose category',
                'style': 'width: 430px; max-width: 500px; outline:none;',
            }),
        }


class BidForm(ModelForm):
    class Meta:
         model = Bids
         fields =('current_bid',)
         labels = {
            "current_bid": ("")
            }
         widgets ={
         'current_bid': forms.NumberInput(attrs={'style': 'width: 545px; outline:none;',}) 
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
                'placeholder': "Add your comment here",
                'style': 'width: 545px; outline:none;',
                'rows': 1
            })
        }



