from django import forms
import decimal

class QueryForm(forms.Form):
	latitude = forms.DecimalField(widget = forms.HiddenInput())
	longitude = forms.DecimalField(widget = forms.HiddenInput())
    
	radius = forms.DecimalField(max_digits=6, decimal_places=3, min_value=decimal.Decimal(0), initial=1.0, \
	                            widget = forms.NumberInput(attrs={'class':'form-control',\
	                                'placeholder':'1.0', 'autofocus':'on'}))
	limit = forms.IntegerField(min_value=0, initial=15, \
								widget = forms.NumberInput(attrs={'class':'form-control',\
	                                'placeholder':'15', 'autofocus':'on'}))

