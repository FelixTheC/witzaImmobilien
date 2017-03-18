from django import forms


class ContactForm(forms.Form):
    ANLIEGEN = (
        ('Angebote', 'Angebote'),
        ('Meine Immobilie', 'Meine Immobilie'),
        ('Bewertung', 'Bewertung'),
        ('Allgemein', 'Allgemein'),
    )
    GENDER = (
        ('Herr', 'Herr'),
        ('Frau', 'Frau'),
        ('Firma', 'Firma'),
    )
    contact_anliegen = forms.ChoiceField(choices=ANLIEGEN, label='Betreff')
    contact_gender = forms.ChoiceField(choices=GENDER, label='Anrede')
    contact_name = forms.CharField(required=True, label='Name')
    contact_email = forms.EmailField(required=True, label='Email')
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Nachricht'
    )


class EstateForm(forms.Form):
    ANLIEGEN = (
        ('Kaufen', 'Kaufen'),
        ('Besichtigung', 'Besichtigung'),
        ('Beratung', 'Beratung'),
    )
    GENDER = (
        ('Herr', 'Herr'),
        ('Frau', 'Frau'),
        ('Firma', 'Firma'),
    )
    contact_anliegen = forms.ChoiceField(choices=ANLIEGEN, label='Betreff')
    contact_gender = forms.ChoiceField(choices=GENDER, label='Anrede')
    contact_name = forms.CharField(required=True, label='Name')
    contact_email = forms.EmailField(required=True, label='Email')
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Nachricht'
    )