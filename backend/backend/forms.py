from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length = 100) # NOTE: this max length is arbitrary placeholder
    real_price = forms.FloatField()
    direct_labor = forms.FloatField() # Consider placing a lower bound of 0.0?
    direct_wages = forms.FloatField()

class DependencyForm(forms.Form):
    # Im not sure how to set this form up, it will be something like this
    # dependent = forms.ModelChoiceField() #This will not be given in the modal, and should be filled in automatically
    # dependency = forms.ModelChoiceField()
    pass