from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import (
    Grower, Farm, PlantPart, Pest, Region,
    SEASON_CHOICES, CONFIDENCE_CHOICES, Disease, Observation
)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    # Removed farm_name field - users will add actual farms after registration
    contact_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Grower.objects.create(
                user=user,
                business_name=f"{user.username}'s Mango Business",  # Provide default business name
                contact_number=self.cleaned_data.get('contact_number')
            )
        return user


class FarmForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label=None,
        required=True
    )

    class Meta:
        model = Farm
        fields = [
            'name',
            'region',
            'geoscape_address_id',
            'formatted_address',
            'size_hectares',
            'stocking_rate'
        ]
        widgets = {
            'geoscape_address_id': forms.HiddenInput(),
            'formatted_address': forms.HiddenInput(),
        }
        labels = {
            'stocking_rate': 'Stocking Rate (plants per hectare)',
        }

    def clean(self):
        cleaned_data = super().clean()
        geoscape_id = cleaned_data.get('geoscape_address_id')
        formatted_addr = cleaned_data.get('formatted_address')

        if geoscape_id and not formatted_addr:
            self.add_error('formatted_address', "If a Geoscape ID is provided, the formatted address must also be present.")
        
        if not geoscape_id:
            cleaned_data['formatted_address'] = ''

        size_hectares = cleaned_data.get('size_hectares')
        stocking_rate = cleaned_data.get('stocking_rate')

        if size_hectares is not None and size_hectares <= 0:
            self.add_error('size_hectares', 'Farm size must be a positive number.')
        
        if stocking_rate is not None and stocking_rate <= 0:
            self.add_error('stocking_rate', 'Stocking rate must be a positive number.')

        return cleaned_data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class GrowerProfileEditForm(forms.ModelForm):
    class Meta:
        model = Grower
        fields = ['business_name', 'contact_number']
        labels = {
            'business_name': 'Business/Company Name',
        }
        help_texts = {
            'business_name': 'The name of your mango growing business or company',
        }


class CalculatorForm(forms.Form):
    farm = forms.ModelChoiceField(
        queryset=Farm.objects.none(),
        label="Select Your Farm",
        empty_label="-- Please Select a Farm --",
        required=True,
    )
    confidence_level = forms.ChoiceField(
        choices=CONFIDENCE_CHOICES,
        required=True,
        label="Desired Confidence Level"
    )

    def __init__(self, grower, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if grower:
            self.fields['farm'].queryset = Farm.objects.filter(owner=grower).order_by('name')
        
        self.fields['farm'].widget.attrs.update({'class': 'form-select form-select-lg mb-2'})
        self.fields['confidence_level'].widget.attrs.update({'class': 'form-select mb-2'})


class ObservationForm(forms.ModelForm):
    pests_observed = forms.ModelMultipleChoiceField(
        queryset=Pest.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Pests Observed at this Plant"
    )
    diseases_observed = forms.ModelMultipleChoiceField(
        queryset=Disease.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Diseases Observed at this Plant"
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    # Make plant_sequence_number hidden and not required from user input
    plant_sequence_number = forms.IntegerField(
        required=False,  # Changed to False since it's auto-generated
        widget=forms.HiddenInput(),  # Hidden since it's auto-generated
        min_value=1
    )

    class Meta:
        model = Observation
        fields = ['plant_sequence_number', 'pests_observed', 'diseases_observed', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the old styling since it's now hidden
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})