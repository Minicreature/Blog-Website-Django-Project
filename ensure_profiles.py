from django.contrib.auth.models import User
from blog.models import Profile

for user in User.objects.all():
    if not hasattr(user, 'profile'):
        print(f"Creating profile for {user.username}")
        Profile.objects.create(user=user, display_name=user.username)
    else:
        print(f"Profile already exists for {user.username}")
