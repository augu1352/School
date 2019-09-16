from django import forms


class TestForm(forms.Form):
    value1 = forms.CharField(label="value1")
    value2 = forms.IntegerField(label="value2")
    
