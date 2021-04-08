from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from auth_accounts.forms import SubscriptionPlanForm,SubscribedEntityForm
from auth_accounts.models import SubscriptionPlanModel
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.urls import reverse_lazy

class SubscriptionPlan_CreateView(CreateView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_add.html'
    fields = ['subscription_type','subscription_plan','duration_val','duration_type','amount_val','amount_type','max_device_limit','max_user_limit','description']

class SubscriptionPlan_UpdateView(UpdateView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_edit.html'
    fields = ['subscription_type','subscription_plan','duration_val','duration_type','amount_val','amount_type','max_device_limit','max_user_limit','description']
    context_object_name = 'subscription_plan'
    

class SubscriptionPlan_ListView(ListView):
    model = SubscriptionPlanModel
    template_name = 'auth_accounts/subscriptionplan_list.html'
    context_object_name = 'subscription_plans'   
    queryset = SubscriptionPlanModel.objects.all()

class SubscriptionPlan_DeleteView(DeleteView):
    model = SubscriptionPlanModel
    # success_url = reverse_lazy('subscriptionplan_list')
    context_object_name = 'subscription_plan'
    pk_url_kwarg = 'pk'
    template_name = 'auth_accounts/subscriptionplan_confirm_delete.html'
    success_url = '/auth_accounts/subscriptionplan_list'


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



                

