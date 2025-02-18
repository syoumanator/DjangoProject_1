from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.EmailField):
                field.widget.attrs.update({"class": "form-control", "type": "email"})
            else:
                field.widget.attrs.update({"class": "form-control"})

class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Введите актуальный адрес электронной почты.'
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Необязательно. Введите актуальный номер телефона.'
    )
    avatar = forms.ImageField(
        required=False,
        help_text='Необязательно. Загрузите изображение для аватарки.'
    )
    country = forms.CharField(
        max_length=15,
        required=False,
        help_text='Необязательно. Введите страну проживания.'
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'avatar', 'country', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number