from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ExtendedUser


class ExtendedUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ExtendedUser
        fields = ('email',)


class ExtendedUserChangeForm(UserChangeForm):

    class Meta:
        model = ExtendedUser
        fields = ('email',)