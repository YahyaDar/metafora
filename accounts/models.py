from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, registeration_number=None, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False, is_student=False, is_faculty=False):
        if not email:
            raise ValueError("You must provide an email address!")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            registeration_number=registeration_number,
        )

        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)

        return user

    def create_student(self, email, registeration_number=None, full_name=None, password=None):
        if not registeration_number:
            raise ValueError("Registeration Number is a required field.")
        user = self.create_user(
            email,
            registeration_number=registeration_number,
            full_name=full_name,
            password=password,
            is_student=True,
        )
        user.save(using=self._db)
        return user

    def create_faculty(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_faculty=True,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, registeration_number=None, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            registeration_number=registeration_number,
            is_staff=True,
            is_admin=True
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    registeration_number = models.PositiveIntegerField(blank=True, null=True, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    student = models.BooleanField(default=False),
    faculty = models.BooleanField(default=False),

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'registeration_number',
        'full_name',
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_student(self):
        return self.student

    @property
    def is_faculty(self):
        return self.faculty
