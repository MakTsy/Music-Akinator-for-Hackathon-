from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(label=False, widget=forms.Textarea(
            attrs={"placeholder": "  Введіть текст пісні...",}
        ))