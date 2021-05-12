from django import forms


class StageForm(forms.Form):
    answer = forms.CharField()
    
