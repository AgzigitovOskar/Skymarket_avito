from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from users.managers import UserManager, UserRoles


class User(AbstractBaseUser):
    objects = UserManager()

    # USER = 'user'
    # ADMIN = 'admin'
    # ROLES = [
    #     (USER, 'пользователь'),
    #     (ADMIN, 'администратор'),
    # ]

    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    # role = models.CharField(max_length=20, choices=ROLES, default=USER)
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_admin(self):
        # return self.role == self.ADMIN
        return self.role == self.UserRoles.ADMIN

    @property
    def is_user(self):
        # return self.role == self.USER
        return self.role == self.UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        ordering = ['email']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.pk}: ({self.first_name} {self.last_name})"


