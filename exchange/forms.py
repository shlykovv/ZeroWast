from django import forms

from exchange.models import ExchangeItem


class ExchangeItemForm(forms.ModelForm):
    class Meta:
        model = ExchangeItem
        fields = [
            'title', 'description', 'category',
            'status', 'image', 'location']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Название'}),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded',
                'rows': 4, 'placeholder': 'Описание'}),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 border rounded'}),
            'status': forms.Select(attrs={
                'class': 'w-full p-2 border rounded'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full p-2 border rounded'}),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Район или адрес'}),
        }
