from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from auth_accounts.forms import SubscriptionPlanForm,SubscribedEntityForm
from auth_accounts.models import SubscriptionPlanModel
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from auth_accounts.models import UserDetailModel
from common.auth_decorator import role_required, company_user, individual_user, admin_user, all_user

i_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), individual_user]
c_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), company_user]
admin_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), admin_user]
all_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), all_user]


@method_decorator(admin_usr_decorators, name="dispatch")
class SubscriptionPlan_CreateView(CreateView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_add.html'
    fields = ['subscription_type', 'subscription_plan', 'duration_val', 'duration_type',
              'amount_val', 'amount_type', 'max_device_limit', 'max_user_limit', 'description']
    success_url = reverse_lazy('subscriptionplan_list')


# # @method_decorator(login_required)
# def dispatch(self, *args, **kwargs):
#     return super().dispatch(*args, **kwargs)


@method_decorator(admin_usr_decorators, name="dispatch")
class SubscriptionPlan_UpdateView(UpdateView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_edit.html'
    fields = ['subscription_type', 'subscription_plan', 'duration_val', 'duration_type',
              'amount_val', 'amount_type', 'max_device_limit', 'max_user_limit', 'description']
    context_object_name = 'subscription_plan'


@method_decorator(all_usr_decorators, name="dispatch")
class SubscriptionPlan_ListView(ListView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_list.html'
    context_object_name = 'subscription_plans'
    queryset = SubscriptionPlanModel.objects.filter(amount_val=222.0)
    # queryset = SubscriptionPlanModel.objects.all()


@method_decorator(all_usr_decorators, name="dispatch")
class SubscriptionPlan_DetailView(DetailView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_detail.html'
    context_object_name = 'subscription_plan'
    queryset = SubscriptionPlanModel.objects.all()


@method_decorator(admin_usr_decorators, name="dispatch")
class SubscriptionPlan_DeleteView(DeleteView):
    model = SubscriptionPlanModel
    context_object_name = 'subscription_plan'
    template_name = 'auth_accounts/subscriptionplan_confirm_delete.html'
    success_url = reverse_lazy('subscriptionplan_list')


# class SubscriptionPlan(View):
#     def get(self,request):
#         subscription_plan_form = SubscriptionPlanForm()
#         return render(request,'auth_accounts/subscriptionplan.html',{'subscription_plan_form':subscription_plan_form})

#     def post(self,request,id):
#         if request.post.get("create"):
#             subscription_plan_form = SubscriptionPlanForm(request.POST)
#             if subscription_plan_form.is_valid():
#                 subscription_plan_form.save()
#         elif request.post.get("update"):
#             obj = get_object_or_404(SubscriptionPlanModel, id = id)
#             subscription_plan_form = SubscriptionPlanForm(request.POST or None,instance=obj)
#             if subscription_plan_form.is_valid():
#                 subscription_plan_form.save()
