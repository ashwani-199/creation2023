from django import forms

from .models import Comment, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'nameid', 'placeholder': 'Name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'emailid', 'placeholder': 'Email'}
        )
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'bodyid'}
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'nameid', 'placeholder': 'Name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'emailid', 'placeholder': 'Email'}
        )
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'phoneid', 'placeholder': 'Phone number'}
        )
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control mb-3', 'id': 'messageid'}
        )
