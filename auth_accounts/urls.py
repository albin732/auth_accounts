
from django.urls import path
from .view.dashboard import Dashboard
from .view.registeration import UserSignUp
# from .view.subscription import SubscriptionPlan
from .view.subscription import SubscriptionPlan_CreateView,SubscriptionPlan_UpdateView,SubscriptionPlan_ListView,SubscriptionPlan_DeleteView

urlpatterns = [
    path('UserSignUp/',UserSignUp.as_view(),name='UserSignUp'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),

    # path('subscription_plan/',SubscriptionPlan.as_view(),name='subscription_plan'),
    path('subscriptionplan_add/', SubscriptionPlan_CreateView.as_view(),
         name='subscriptionplan_add'),
    path('subscriptionplan_edit/<int:pk>/', SubscriptionPlan_UpdateView.as_view(),
         name='subscriptionplan_edit'),
    path('subscriptionplan_list/', SubscriptionPlan_ListView.as_view(),
         name='subscriptionplan_list'),
    path('subscriptionplan_delete/<int:pk>/', SubscriptionPlan_DeleteView.as_view(),
         name='subscriptionplan_delete'),
]
