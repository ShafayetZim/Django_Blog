from django import forms

from .models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'name', 'age', 'address', 'salary', 'email',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
