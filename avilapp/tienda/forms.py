from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingresa tu nombre.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Requerido. Ingresa tu apellido.")
    email = forms.EmailField(max_length=254, required=True, help_text="Requerido. Ingresa una dirección de correo electrónico válida.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(label='', max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        del self.fields['password']

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>50 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.</small></span>'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Ingresa tu nombre.</small></span>'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Ingresa tu apellido.</small></span>'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>Ingresa una dirección de correo electrónico válida.</small></span>'

class ReservaProfileForm(UserChangeForm):
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(label='', max_length=50,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(ReservaProfileForm, self).__init__(*args, **kwargs)

        del self.fields['password']

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

