from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from auth_accounts.forms import UserSignUpForm, UserDetailForm
# from auth_accounts.models import UserDetail
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserSignUp(View):

    def get(self, request):
        user_form = UserSignUpForm()
        userdetail_form = UserDetailForm()
        return render(request, 'auth_accounts/UserSignUp.html', {'user_form': user_form, 'userdetail_form': userdetail_form})

    def post(self, request):
        user_form = UserSignUpForm(request.POST)
        userdetail_form = UserDetailForm(request.POST)
        if user_form.is_valid() and userdetail_form.is_valid():
            user = user_form.save()
            # user.userdetail.user_type = userdetail_form.cleaned_data.get('user_type')
            user.userdetail.user_type = '3'  # IndividualUser
            user.userdetail.contact_number = userdetail_form.cleaned_data.get(
                'contact_number')
            user.userdetail.save()
            # add permission_group
            iusr_group = Group.objects.get(name='individual_user_perm')
            iusr_group.user_set.add(user)

            messages.success(request, 'Account created successfully')
            return redirect('/auth_accounts/UserSignUp')
        messages.success(request, 'Validation Error')
        return render(request, 'auth_accounts/UserSignUp.html', {'user_form': user_form, 'userdetail_form': userdetail_form})
