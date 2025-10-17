from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='Force reseed (truncate) before insert')

    def handle(self, *args, **options):
        force = options.get('force')
        self.stdout.write(self.style.NOTICE('Starting seed...'))
        # TODO: implement your seed logic here (users, roles, fixtures)
        # Example:
        # from apps.users.models import User
        # User.objects.get_or_create(email='admin@example.com', defaults={'is_staff': True})
        self.stdout.write(self.style.SUCCESS('Seed completed.'))
