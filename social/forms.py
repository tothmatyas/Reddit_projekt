from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Felhasználónév',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add meg a felhasználóneved'
        }),
        help_text=''
    )

    password1 = forms.CharField(
        label='Jelszó',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add meg a jelszavad'
        }),
        help_text=''
    )

    password2 = forms.CharField(
        label='Jelszó megerősítése',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Írd be újra a jelszót'
        }),
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Felhasználónév',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Felhasználónév'
        })
    )

    password = forms.CharField(
        label='Jelszó',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Jelszó'
        })
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Cím',
            'content': 'Tartalom',
            'image': 'Kép'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poszt címe'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Írd le, amit szeretnél...', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Komment'
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Írj kommentet...',
                'rows': 3
            })
        }
