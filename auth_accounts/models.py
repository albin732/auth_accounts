from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from datetime import datetime, timedelta


# User._meta.get_field('email')._unique = True


class UserDetailModel(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'admin'),
        ('company_user', 'company_user'),
        ('individual_user', 'individual_user')
    )
    user = models.OneToOneField(
        User, related_name='userdetail', on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=30, choices=USER_TYPE_CHOICES, default='individual_user')
    contact_number = models.CharField(max_length=15, blank=True)

    # profile_img = models.ImageField(upload_to ='images/user_images', blank=True, null=True)

    class Meta:
        db_table = "userdetail"

    def __str__(self):
        return str(self.user)

    def usr_type(self):
        return str(self.user_type)

    def save(self, *args, **kwargs):
        super(UserDetailModel, self).save(*args, **kwargs)


class SubscriptionPlanModel(models.Model):
    SUBSCRIPTION_TYPE_CHOICES = [('1', 'Company'), ('2', 'Individual User'), ]
    DURATION_TYPE_CHOICES = [('1', 'Day'), ('2', 'Month'), ('3', 'Year')]
    AMOUNT_TYPE_CHOICES = [('1', 'INR'), ('2', 'USD')]
    subscription_type = models.CharField(
        max_length=100, choices=SUBSCRIPTION_TYPE_CHOICES, default=2)
    subscription_plan = models.CharField(
        max_length=100, blank=False, null=False, unique=True, verbose_name="Plan Name")
    duration_val = models.CharField(max_length=10, blank=True)
    duration_type = models.CharField(
        max_length=15, choices=DURATION_TYPE_CHOICES, default=1)
    amount_val = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True)
    amount_type = models.CharField(
        max_length=15, choices=AMOUNT_TYPE_CHOICES, default=1)
    max_device_limit = models.IntegerField()
    max_user_limit = models.CharField(max_length=15, blank=True)
    description = models.TextField()

    class Meta:
        db_table = "subscription_plan"


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=150)
    company_email = models.EmailField(max_length=100, unique=True, blank=False)
    contact_person = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    company_address = models.TextField()

    class Meta:
        db_table = "company"


class SubscribedEntityModel(models.Model):
    subscription = models.ForeignKey(
        SubscriptionPlanModel, on_delete=models.CASCADE)
    company = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    subscription_start_date = models.DateField(
        blank=False, default=datetime.now()+timedelta(days=15))
    subscription_end_date = models.DateField(
        blank=False, default=datetime.now())

    class Meta:
        db_table = "subscribed_entity"
