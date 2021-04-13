from django.contrib.auth.models import Group


def add_permission_group(self, request):
    admin_master = Group.objects.create(name='admin_master_perm')
    admin_user = Group.objects.create(name='admin_user_perm')
    company_master = Group.objects.create(name='company_master_perm')
    company_user = Group.objects.create(name='company_user_perm')
    individual_user = Group.objects.create(name='individual_user_perm')


def assign_permission_to_group(self, request):
    admin_master.permissions.add(perm1, perm3, perm4)


def assign_user_to_group(self, request):
    admin_master.user_set.add(user1, user2, user5, user7)
