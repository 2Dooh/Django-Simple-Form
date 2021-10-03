from django import forms
from django.forms import widgets

class SimpleForm(forms.Form):

    name = forms.CharField(
        max_length=200,
        required=True, 
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='Email',
        max_length=50,
        required=True,
        widget=forms.EmailInput()
    )
    birth_day = forms.DateTimeField(
        label='Date of birth',
        required=True,
        widget=forms.DateTimeInput()
    )
    gender = forms.NullBooleanField(
        label='Gender',
        widget=forms.RadioSelect(
            choices=[(True, 'Male'), (False, 'Female'), ('', 'Others')], 
        )
    )
    occupation = forms.ChoiceField(
        choices=[
            ('student', 'Student'),
            ('employee', 'Employee'),
            ('lecturer', 'Lecturer'),
            ('prefer_no', 'Other')
        ],
        widget=forms.Select(),
    )
    recommend = forms.NullBooleanField(
        widget=forms.RadioSelect(
            choices=[(True, 'Yes'), (False, 'No'), ('', 'Maybe')]
        )
    )
    subjects = forms.MultipleChoiceField(
        choices=[
            ('front-end-projects', 'Front-end Projects'),
            ('back-end-projects', 'Back-end Projects'),
            ('data-visualization', 'Data Visualization'),
            ('open-source-community', 'Open Source Community')
        ],
        widget=forms.CheckboxSelectMultiple()
    )
    comment = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-group'})