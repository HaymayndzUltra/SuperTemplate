from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Bootstrap initial application data. Optionally create a default superuser."

    def add_arguments(self, parser):
        parser.add_argument(
            "--with-admin",
            action="store_true",
            help="Create a default superuser (admin@example.com / generated password)",
        )
        parser.add_argument(
            "--email",
            default="admin@example.com",
            help="Email for the bootstrap superuser (default: admin@example.com)",
        )

    def handle(self, *args, **options):
        # Place any domain bootstrapping logic here (fixtures, reference data, etc.)
        self.stdout.write(self.style.SUCCESS("✓ Application bootstrap completed."))

        if options.get("with_admin"):
            User = get_user_model()
            email = options.get("email")
            if not User.objects.filter(email=email).exists():
                password = get_random_string(16)
                user = User.objects.create_superuser(
                    email=email,
                    password=password,
                    first_name="Admin",
                    last_name="User",
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✓ Created superuser {email} with password: {password}\n⚠️  Store this password securely or change it immediately."
                    )
                )
            else:
                self.stdout.write(self.style.WARNING(f"Superuser {email} already exists; skipping."))
