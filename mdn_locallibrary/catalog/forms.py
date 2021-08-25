from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy
import datetime  # for checking renewal date range.

from django import forms

from catalog.models import BookInstance


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""
    renewal_date = forms.DateField(
            help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(ugettext_lazy('Invalid date - renewal in past'))
        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                ugettext_lazy('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


# class RenewBookModelForm(ModelForm):
#     def clean_due_back(self):
#        data = self.cleaned_data['due_back']
#
#        if data < datetime.date.today():
#            raise ValidationError(ugettext_lazy('Invalid date - renewal in past'))
#
#        if data > datetime.date.today() + datetime.timedelta(weeks=4):
#            raise ValidationError(ugettext_lazy('Invalid date - renewal more than 4 weeks ahead'))
#
#        return data
#
#     class Meta:
#         model = BookInstance
#         fields = ['due_back',]
#         labels = { 'due_back': ugettext_lazy('Renewal date'), }
#         help_texts = { 'due_back': ugettext_lazy('Enter a date between now and 4 weeks (default 3).'), }
