from apps.Villager.models import Villager, Remark
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper


class DateInput(forms.DateInput):
    input_type = 'date'


class VillagerForm(ModelForm):
    class Meta:
        model = Villager
        fields = '__all__'
        widgets = {
            'next_follow_up_date': DateInput(attrs={'type': 'date'}),
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(VillagerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True


class VillagerNextFollowUpForm(ModelForm):
    class Meta:
        model = Villager
        fields = ['next_follow_up_date',]
        widgets = {
            'next_follow_up_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(VillagerNextFollowUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True


class RemarkForm(ModelForm):
    class Meta:
        model = Remark
        fields = ['remark']
