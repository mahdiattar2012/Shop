from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password, code):
        if not username:
            raise ValueError('Please enter a username')
        if not email:
            raise ValueError('Please enter your email')
        user = self.model(first_name=first_name, last_name=last_name,
                          username=username, email=self.normalize_email(email), code = code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password, code = ''):
        user = self.create_user(first_name, last_name,
                                username, email, password, code)
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user
