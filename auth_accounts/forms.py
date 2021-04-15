from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from django.core.exceptions import ValidationError
from .models import UserDetailModel, SubscriptionPlanModel, SubscribedEntityModel


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Full name")
    exclude = ('email',)
    username = forms.EmailField(max_length=64,
                                help_text="email address.", label='Email')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'first_name']


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetailModel
        fields = ('contact_number',)


# class SubscriptionPlanForm(forms.ModelForm):
#     class Meta:
#         model = SubscriptionPlanModel
#         fields = '__all__'
        # fields = ['subscription_type','subscription_plan','duration_val','duration_type','amount_val','amount_type','max_device_limit','max_user_limit','description']


# class SubscribedEntityForm(forms.ModelForm):
#     class Meta:
#         model = SubscribedEntityModel
#         fields = '__all__'
