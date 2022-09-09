from dataclasses import field
from django import forms

from . models import User


class EnskripsyonForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'modpass')
    def clean(self):
        clean_data = super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data['username']
        modpass = self.cleaned_data['modpass']

        if len(first_name) < 2:
            self.add_error("first_name", "first_name is not ok")
        
        if len(last_name) < 2:
            self.add_error("last_name", "last_name is not ok")

        if len(username) > 10:
            self.add_error("username", "your Username is too long")
        
        if len(modpass.split(" ")) > 1:
            self.add_error("password", "please put one words")