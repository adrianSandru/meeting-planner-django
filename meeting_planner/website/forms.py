from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    #username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({ 'class' : 'form-control input-sm',
                                                        'type' : 'text',
                                                        'name' : 'username',
                                                        'id' : 'username',
                                                        'placeholder' : 'Username'})
        self.fields['first_name'].widget.attrs.update({ 'class' : 'form-control input-sm',
                                                        'type' : 'text',
                                                        'name' : 'first_name',
                                                        'id' : 'first_name',
                                                        'placeholder' : 'First Name'})
        
        self.fields['last_name'].widget.attrs.update({  'class' : 'form-control input-sm',
                                                        'type' : 'text',
                                                        'name' : 'last_name',
                                                        'id' : 'last_name',
                                                        'placeholder' : 'Last Name'})
        
        self.fields['email'].widget.attrs.update({  'class' : 'form-control input-sm',
                                                    'type' : 'text',
                                                    'name' : 'email',
                                                    'id' : 'email',
                                                    'placeholder' : 'Email'})

        self.fields['password1'].widget.attrs.update({ 'class' : 'form-control input-sm',
                                                        'type' : 'text',
                                                        'name' : 'password1',
                                                        'id' : 'password1',
                                                        'placeholder' : 'Password'})                                                          
        
        self.fields['password2'].widget.attrs.update({ 'class' : 'form-control input-sm',
                                                       'type' : 'text',
                                                       'name' : 'password2',
                                                       'id' : 'password2',
                                                       'placeholder' : 'Repeat Password'})
