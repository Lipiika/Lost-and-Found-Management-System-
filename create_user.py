import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lostfoundmanagement.settings")
django.setup()

from django.contrib.auth.models import User

# Create admin
User.objects.create_superuser(username='adminlipika', password='adminpass123', email='admin@example.com')

# Create random normal users
import random
import string

for i in range(5):
    username = 'user' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    user = User.objects.create_user(username=username, password=password)
    print(f"Created user -> Username: {username}, Password: {password}")


