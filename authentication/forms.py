from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True,
    label="Username",
    max_length=100,
    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Username"})
    )

    password1=forms.CharField(required=True,
    label="Password",
    max_length=100,
    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Password","type":"password"})
    )

    password2=forms.CharField(required=True,
    label="Confirm Password",
    max_length=100,
    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Confirm Your Password","type":"password"})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1)<8:
            raise forms.ValidationError("Password must contain alteast 8 characters")
        return password1

    def clean(self):
        cleaned_data = super().clean()
        if 'password1' in cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 != password2:
                raise forms.ValidationError({"password2":"Passwords didn't match"})
        return cleaned_data

    class Meta:
        model = User
        fields = ['username']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):

    username = forms.CharField(required=True,
    label="Username",
    max_length=100,
    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Username"})
    )

    password=forms.CharField(required=True,
    label="Password",
    max_length=100,
    widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Password","type":"password"})
    )
