from django.core.management.base import BaseCommand
from core.models import User
import os

class Command(BaseCommand):
    help = 'Create or update superuser for remote deployment'

    def handle(self, *args, **options):
        email = 'javohirqobiljonov32@gmail.com'
        password = 'javohir2010007'
        first_name = 'Javohir'
        last_name = 'Qobiljonov'
        
        self.stdout.write(f'Checking for superuser: {email}...')
        
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )
        
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" created successfully!'))
        else:
            # Update existing user to be sure they have admin rights
            user.is_staff = True
            user.is_superuser = True
            user.role = 'admin'
            user.is_active = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" updated successfully!'))
