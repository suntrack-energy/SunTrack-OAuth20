from django import forms

class LoginForms(forms.Form):
    email_login = forms.CharField(
        label="E-mail",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu e-mail'
            }
        ),
    )
    senha_login = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu nome'
            }
        ),
    )
    sobrenome_cadastro = forms.CharField(
        label='Sobrenome',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu sobrenome'
            }
        ),
    )
    email_cadastro = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu email'
            }
        ),
    )
    senha1_cadastro = forms.CharField(
        label='Crie uma senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite a senha'
            }
        ),
    )
    senha2_cadastro = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirme a senha'
            }
        ),
    )

    def clean_senha_cadastro2(self):
        senha1_cadastro = self.cleaned_data.get('senha1_cadastro')
        senha2_cadastro = self.cleaned_data.get('senha2_cadastro')

        if senha1_cadastro and senha2_cadastro:
            if senha1_cadastro != senha2_cadastro:
                    raise forms.ValidationError('As senhas não são iguais')
            else:
                 return senha2_cadastro