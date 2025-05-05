from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

def save(self, commit=False):
    user = super().save(commit=False)
    user.username = f"{self.cleaned_data['first_name']}{self.cleaned_data['email']}"
    if commit:
        user.save()
    return user

def clean_password(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Проверьте пароли')
        return pass2
    
def clean_name(self):
    return self.cleaned_data['first_name']

def clean_surname(self):
    return self.cleaned_data['last_name']

def init(self, args, **kwargs):
    super(RegistrationForm, self).init(args, **kwargs)
    self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
    self.fields['email'].widget.attrs['placeholder'] = 'Почта'
    self.fields['phone'].widget.attrs['placeholder'] = 'Номер телефона'
    self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
    self.fields['password2'].widget.attrs['placeholder'] = 'Подтверждение'

    self.fields['password1'].widget.attrs['id'] = 'password-input'
    self.fields['password2'].widget.attrs['id'] = 'password-input'