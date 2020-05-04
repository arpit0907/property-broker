from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create Pre-defined Roles and Permissions'

    def handle(self, *args, **options):

        predefined_roles = ['Owner','Renter']
        for role in predefined_roles:
            group, created = Group.objects.get_or_create(name=role)
            
        self.stdout.write(self.style.WARNING('Successfully Done'))


# from django.contrib.auth.models import User
# from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#     help = 'Delete users'

#     def add_arguments(self, parser):
#         parser.add_argument('user_id', nargs='+', type=int, help='User ID')

#     def handle(self, *args, **kwargs):
#         users_ids = kwargs['user_id']

#         import pdb; pdb.set_trace()
#         for user_id in users_ids:
#             try:
#                 user = User.objects.get(pk=user_id)
#                 user.delete()
#                 self.stdout.write(self.style.SUCCESS('User "%s (%s)" deleted with success!' % (user.username, user_id)))
#             except User.DoesNotExist:
#                 self.stdout.write(self.style.WARNING('User with id "%s" does not exist.' % user_id))
#         