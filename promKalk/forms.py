from django import forms


class PromilleForm(forms.Form):
    start_promille = forms.DecimalField()
    antall_timer = forms.IntegerField(min_value=1, max_value=24)
    vekt = forms.IntegerField(min_value=20, max_value=150)
