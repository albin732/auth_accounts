from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import user_passes_test


# groups
def group_required(*group_names):
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)


# roles
def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.userdetail.user_type in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator


def admin_master_only(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.userdetail.user_type == 'admin_master':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def admin_user(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ['admin_master', 'admin_user', 'company_master']
        if request.user.userdetail.user_type in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def company_master(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ['admin_master', 'admin_user', 'company_master']
        if request.user.userdetail.user_type in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def company_user(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ['admin_master', 'admin_user',
                         'company_master', 'company_user']
        if request.user.userdetail.user_type in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def individual_user(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ['admin_master', 'admin_user', 'individual_user']
        if request.user.userdetail.user_type in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def all_user(view_func):
    def wrap(request, *args, **kwargs):
        allowed_roles = ['admin_master', 'admin_user',
                         'company_master', 'company_user', 'individual_user']
        if request.user.userdetail.user_type in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


# from django.contrib.auth.decorators import login_required

# def is_iusr(self,request):
#     user = self.request.user
#     usr_type = user.userdetail.user_type
#     if user_type == 'IndividualUser':
#         return True
#     else:
#         return False


# iuser_login_required = user_passes_test(lambda u: True if u.is_iusr else False, login_url='/auth_accounts/login')


# def Iusr_login_required(view_func):
#     decorated_view_func = login_required(
#         rec_login_required(view_func), login_url='/auth_accounts/login')
#     return decorated_view_func


# #  using
# @Iusr_login_required
# def index(request):
#     return render(request, 'index.html')
