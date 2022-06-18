from django import forms
from .models import Demographic, Baseline, Treatment, Diagnostic, Administration

class DemogForm(forms.ModelForm):
    class Meta:
        model = Demographic
        fields = '__all__'

class BaseForm(forms.ModelForm):
    class Meta:
        model = Baseline
        fields = '__all__'

class TxForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class DiagForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = '__all__'

class TimepointForm(forms.ModelForm):
    class Meta:
        model = Administration
        fields = '__all__'