from datetime import datetime, timedelta, time

from django import forms
from django.utils import timezone

from .models import KeyImage
from .base64toimg import stringToRGB


class KeyImageCreateForm(forms.ModelForm):
    class Meta:
        model = KeyImage
        fields = ('user_uuid', 'key_uuid', 'key_img')

    def get_commit_data(self):
        print(self)
        keyimage = super(KeyImageCreateForm, self).save(commit=False)

        return keyimage


class KeyImageCompareForm(forms.Form):
    user_uuid = forms.CharField(max_length=5000)
    key_img = forms.CharField(widget=forms.Textarea)

    def get_data(self):
        print(self)
        if self.is_valid():
            img_tmp = stringToRGB(bytes(self.cleaned_data['key_img'], 'utf-8'))
            return img_tmp, self.cleaned_data['user_uuid']
        return None
