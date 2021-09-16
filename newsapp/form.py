from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class RegistForm(forms.Form):
    ID=forms.CharField(
        label="使用者名稱",
        widget=forms.TextInput(attrs={'id':'uid'})
    )
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    checkpassword=forms.CharField(
        lable="確認密碼",
        widget=forms.PasswordInput(attrs={'class':'form-doublecheck'})
    )
    email=forms.EmailField(
        label="電子信箱",
        widget=forms.widgets.EmailInput(attrs={'id','eid'})
    )
