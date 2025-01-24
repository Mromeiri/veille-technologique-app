from django import forms

class ArxivSearchForm(forms.Form):
    mot_cle = forms.CharField(label="Mot-clé", max_length=100, required=True)
    date_debut = forms.DateField(
        label="Date de début", 
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control date-field',
                'data-placeholder': 'Sélectionner la date de début',
                'aria-label': 'Date de début'
            }
        )
    )
    date_fin = forms.DateField(
        label="Date de fin", 
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control date-field',
                'data-placeholder': 'Sélectionner la date de fin',
                'aria-label': 'Date de fin'
            }
        )
    )




class ScholarSearchForm(forms.Form):
    mot_cle = forms.CharField(label='Mot-clé', max_length=100)
    date_debut = forms.DateField(label="Date de début", widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    date_fin = forms.DateField(label="Date de fin", widget=forms.DateInput(attrs={'type': 'date'}), required=True)

class ScholarsemSearchForm(forms.Form):
    mot_cle = forms.CharField(max_length=100)


class PLOSOneSearchForm(forms.Form):
    mot_cle = forms.CharField(label="Mot-clé", max_length=100)
    date_debut = forms.DateField(
        label="Date de début", 
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control date-field',
                'data-placeholder': 'Sélectionner la date de début',
                'aria-label': 'Date de début'
            }
        )
    )
    date_fin = forms.DateField(
        label="Date de fin", 
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control date-field',
                'data-placeholder': 'Sélectionner la date de fin',
                'aria-label': 'Date de fin'
            }
        )
    )