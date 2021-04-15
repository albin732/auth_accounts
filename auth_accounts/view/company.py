from django.contrib.auth.decorators import login_required

# from auth_accounts.forms import SubscriptionPlanForm,SubscribedEntityForm
from auth_accounts.models import CompanyModel

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from auth_accounts.models import UserDetailModel
from common.auth_decorator import group_required, role_required, company_user, individual_user, admin_user, all_user

i_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), individual_user]
c_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), company_user]
admin_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), admin_user, group_required('admin',)]
all_usr_decorators = [login_required(
    login_url='/auth_accounts/login/'), all_user]


@method_decorator(admin_usr_decorators, name="dispatch")
class Company_CreateView(CreateView):
    model = CompanyModel
    template_name = 'auth_accounts/company_add.html'
    fields = ['company_name', 'company_email', 'contact_person', 'contact_number',
              'company_address']
    success_url = reverse_lazy('company_list')


@method_decorator(admin_usr_decorators, name="dispatch")
class Company_UpdateView(UpdateView):
    model = CompanyModel
    template_name = 'auth_accounts/subscriptionplan_edit.html'
    fields = ['company_name', 'company_email', 'contact_person', 'contact_number',
              'company_address']
    context_object_name = 'company_list'


@method_decorator(admin_usr_decorators, name="dispatch")
class Company_DeleteView(DeleteView):
    model = CompanyModel
    context_object_name = 'company'
    template_name = 'auth_accounts/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


@method_decorator(admin_usr_decorators, name="dispatch")
class Company_ListView(ListView):
    model = CompanyModel
    template_name = 'auth_accounts/company_list.html'
    context_object_name = 'companies'
    queryset = CompanyModel.objects.all()


@method_decorator(admin_usr_decorators, name="dispatch")
class Company_DetailView(DetailView):
    model = CompanyModel
    template_name = 'auth_accounts/company_detail.html'
    context_object_name = 'company'
    queryset = CompanyModel.objects.all()
