from django import forms

from greenpoints.models import GreenPoint


class GreenPointForm(forms.ModelForm):
    class Meta:
        model = GreenPoint
        fields = ['name', 'description', 'latitude', 'longitude']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name, field in self.fields.items():
                if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.update({
                        'rows': 3,
                    })
                field.widget.attrs.update({
    'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-400'
})
