from django.views import View
from django.shortcuts import render

class Dashboard(View):
    def get(self,request):
        return render(request, "auth_accounts/dashboard.html")