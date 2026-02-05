from django  import forms

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name =  forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text = "enter6 digit roll mumber")
    password = forms.CharField(widget = forms.PasswordInput)