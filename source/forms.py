import datetime

from django import forms

from source.models import AnimeModel


class AnimeForm(forms.ModelForm):
    date_format = ['%b %Y']
    start_date = forms.DateField(input_formats=date_format)
    end_date = forms.DateField(input_formats=date_format)

    class Meta:
        model = AnimeModel
        fields = '__all__'

    def get_date(self, str_date):
        return datetime.datetime.strptime(str_date, self.date_format).date()
