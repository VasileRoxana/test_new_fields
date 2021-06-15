from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['age'].required = True
        self.fields['birth_month'].required = True
        self.fields['sex'].required = True
        self.fields['studies'].required = True
        self.fields['job'].required = True
        self.fields['expectations'].required = True
        self.fields['user_environment'].required = True
        

    class Meta(object):
        model = ExtraInfo
        fields = ('age', 'birth_month', 'sex','studies','job','expectations','user_environment')
        labels = {'age': _("Varsta"), 'birth_month': _("Luna nasterii"), 'sex': _("Sex"),'job': _("Job"),'studies': _("Studii"),'expectations': _("Asteptari in urma absolvirii"),'user_environment': _("Mediu")}
        help_text = {'age': _("Te rugam selectează o optiune"), 'birth_month': _("Te rugam selectează o optiune"), 'sex': _("Te rugam selectează o optiune"),'studies': _("Te rugam selectează o optiune"),'expectations': _("Te rugam selectează o optiune"), 'user_environment': _("Te rugam selectează o optiune")}
