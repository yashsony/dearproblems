from django import forms
from django.contrib.auth.models import User
from .models import post
from .models import Comment
from .models import search


class PostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email' ,'username','password','confirm_password')

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        password = cleaned_data.get('password')

        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' % (str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('password_confirm', msg)
        return cleaned_data

class qwe(forms.ModelForm):

    class Meta:
        model = post
        fields =('title','description')

class addcomment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment' ,)

class sea(forms.ModelForm):
    class Meta:
        model = search
        fields = ('q',)