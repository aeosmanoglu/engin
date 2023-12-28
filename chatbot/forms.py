from django import forms


class InputForm(forms.Form):
    input_text = forms.CharField(label='Your Question', max_length=500)
