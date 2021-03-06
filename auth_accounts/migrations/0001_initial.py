# Generated by Django 3.1.7 on 2021-04-08 13:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('company_email', models.EmailField(max_length=100, unique=True)),
                ('contact_person', models.CharField(blank=True, max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('company_address', models.TextField()),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(choices=[('1', 'Company'), ('2', 'Individual User')], default=2, max_length=100)),
                ('subscription_plan', models.CharField(max_length=100, unique=True, verbose_name='Plan Name')),
                ('duration_val', models.CharField(blank=True, max_length=10)),
                ('duration_type', models.CharField(choices=[('1', 'Day'), ('2', 'Month'), ('3', 'Year')], default=1, max_length=15)),
                ('amount_val', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('amount_type', models.CharField(choices=[('1', 'INR'), ('2', 'USD')], default=1, max_length=15)),
                ('max_device_limit', models.IntegerField()),
                ('max_user_limit', models.CharField(blank=True, max_length=15)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'subscription_plan',
            },
        ),
        migrations.CreateModel(
            name='UserDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('admin', 'admin'), ('company_user', 'company_user'), ('individual_user', 'individual_user')], default='individual_user', max_length=30)),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userdetail', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userdetail',
            },
        ),
        migrations.CreateModel(
            name='SubscribedEntityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_start_date', models.DateField(default=datetime.datetime(2021, 4, 23, 13, 37, 57, 513152))),
                ('subscription_end_date', models.DateField(default=datetime.datetime(2021, 4, 8, 13, 37, 57, 513193))),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_accounts.companymodel')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_accounts.subscriptionplanmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subscribed_entity',
            },
        ),
    ]
