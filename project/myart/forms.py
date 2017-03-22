from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
    	username = self.cleaned_data.get("Username")
    	password = self.cleaned_data.get("Password")
    	user = authenticate(username=username, password= password)
    	if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
        
class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(label='Full Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    
    class Meta:
        model = User
        fields = [
            'name',
            'username',
            'email',
            'password',
            'password2',
        ]
    def clean(self, *args, **kwargs):
        email = forms.EmailField(label='Email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already been registered")
            
        return super(UserRegisterForm,self).clean(*args, **kwargs)
