from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class Dashboard(View):

    # @login_required(login_url='/auth_accounts/login/')
    def get(self, request):
        return render(request, "auth_accounts/dashboard.html")
