from django.contrib.auth.models import BaseUserManager


class ContactManager(BaseUserManager):
    def create_contact(self, name, email, subject, message):
        contact = self.model(name=name, email=self.normalize_email(email),
                          subject=subject, message=message)
        contact.save(using=self._db)
        return contact