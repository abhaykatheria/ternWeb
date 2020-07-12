from django import forms

FORMATS =( 
    ("html", "HTML"), 
    ("Default", "TXT"), 
    ("json", "JSON")
)

class NameForm(forms.Form):
    image_name = forms.CharField(label="image name",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','id':'image'}))
    geeks_field = forms.ChoiceField(label="Format",choices = FORMATS,widget=forms.Select(attrs={'class': 'form-control form-control-lg','id':'format'}))