from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label="Recipient Email")
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
