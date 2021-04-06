from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


# create account manager
class UserAccountManager(UserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError('User must have username')
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(email=self.normalize_email(email),
                                username=username,
                                password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active=True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=False)
    email = models.EmailField(verbose_name="email",
                              max_length=254,
                              unique=True)
    country = CountryField(blank=True, null=True)
    profile_picutre = models.ImageField(upload_to="images/",
                                        blank=True,
                                        null=True,
                                        default='images/avatardefault.png')
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'01[0125][0-9]{8}',
                message=
                "Enter a valid Egyption mobile phone number starting with +(country code)"
            ),
        ],
    )
    is_active = models.BooleanField(default=False) 
    birth_date = models.DateField(auto_now=False,
                                  auto_now_add=False,
                                  null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserAccountManager()

    def _str_(self):
        return self.email

    def has_module_perms(self, app_label):
        return True
