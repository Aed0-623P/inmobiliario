from django.test import TestCase

# Create your tests here.

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from inmobiliaria.models import Usuario

class Command(BaseCommand):
    help = 'Populate auth_user with data from Usuario model'

    def handle(self, *args, **options):
        usuarios = Usuario.objects.all()

        for usuario in usuarios:
            # Create a new User instance with data from Usuario model
            new_user = User.objects.create(
                username=usuario.username,  # Provide a username value
                first_name=usuario.nombres,
                last_name=usuario.apellidos,
                email=usuario.correo_electronico
            )
            new_user.set_unusable_password()  # Set an unusable password
            new_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created auth_user instance for {usuario.nombres} {usuario.apellidos}'))