
from .view.logs import Login, Logout
from django.urls import path
from .view.dashboard import Dashboard
from .view.registeration import UserSignUp
# from .view.subscription import SubscriptionPlan
from .view.subscription import SubscriptionPlan_CreateView, SubscriptionPlan_UpdateView, SubscriptionPlan_ListView, SubscriptionPlan_DeleteView, SubscriptionPlan_DetailView
from .view.company import Company_CreateView, Company_UpdateView, Company_ListView, Company_DeleteView, Company_DetailView

urlpatterns = [
    path('UserSignUp/', UserSignUp.as_view(), name='UserSignUp'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # path('subscription_plan/',SubscriptionPlan.as_view(),name='subscription_plan'),
    path('subscriptionplan_add/', SubscriptionPlan_CreateView.as_view(),
         name='subscriptionplan_add'),
    path('subscriptionplan_list/', SubscriptionPlan_ListView.as_view(),
         name='subscriptionplan_list'),
    path('subscriptionplan_detail/<int:pk>/', SubscriptionPlan_DetailView.as_view(),
         name='subscriptionplan_detail'),
    path('subscriptionplan_edit/<int:pk>/', SubscriptionPlan_UpdateView.as_view(),
         name='subscriptionplan_edit'),
    path('subscriptionplan_delete/<int:pk>/', SubscriptionPlan_DeleteView.as_view(),
         name='subscriptionplan_delete'),


    path('company_add/', Company_CreateView.as_view(),
         name='company_add'),
    path('company_list/', Company_ListView.as_view(),
         name='company_list'),
    path('company_detail/<int:pk>/', Company_DetailView.as_view(),
         name='company_detail'),
    path('company_edit/<int:pk>/', Company_UpdateView.as_view(),
         name='company_edit'),
    path('company_delete/<int:pk>/', Company_DeleteView.as_view(),
         name='company_delete'),
]
