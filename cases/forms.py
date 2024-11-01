from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'fullname', 'phonenumber', 'address', 'sex', 'email', 
            'occupation', 'state', 'evidence', 'case_type', 
            'description', 'code'
        ]


class CaseEditForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'fullname', 'phonenumber', 'address', 'sex', 'email', 
            'occupation', 'state', 'evidence', 'case_type', 
            'description', 'status', 'code'
        ]