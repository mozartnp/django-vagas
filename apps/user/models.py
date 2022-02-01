from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    '''
    Class que criar o usuario, necessario para criação de um usuario customizado.
    '''
    def create_user(self, email, tipo_user, password=None):
        if not email:
            raise ValueError("É obrigatório o e-mail.")
        if not tipo_user:
            raise ValueError("É necessario definir se é empresa ou candidato.")

        user = self.model(
            email = self.normalize_email(email),
            tipo_user = tipo_user,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, tipo_user, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            tipo_user = tipo_user,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    '''
    Modelo para criar um usuario customizado pelo django
    '''

    class UserTipo(models.TextChoices):
        '''
        Tipos de escolha do usuario 
        '''
        EMPRESA = 'EMPR', _('Empresa')
        CANDIDATO = 'CAND', _('Candidato')

    email = models.EmailField(max_length=100, unique=True)
    tipo_user = models.CharField(max_length=4,choices=UserTipo.choices)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tipo_user', ]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True