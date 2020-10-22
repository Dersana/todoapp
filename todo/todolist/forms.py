from django import forms

class TodoItem(forms.Form):
    text = forms.CharField(max_length=50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a task', 'aria-label':'todo', 'aria-describedby':'add-btn'}))
