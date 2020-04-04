import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Q


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    nickname = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return f"{self.username}"

    def get_nickname(self):
        return f"{self.nickname}"


class ProfileManager(models.Manager):
    def for_user(self, user):
        try:
            return user.profile
        except UserProfile.DoesNotExist:
            profile = UserProfile(owner=user)
            profile.save()
            return profile


class UserProfile(models.Model):
    owner = models.OneToOneField(User, models.CASCADE, blank=True, null=True, related_name="profile")
    bio = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(blank=True)
    url = models.URLField(blank=True)
    # role = models

    objects = ProfileManager()

    def __str__(self):
        return f"Profile for {self.owner.username}"

    @property
    def owner_profile(self):
        return UserProfile.objects.for_user(self.owner)

    def send_change_email_link(self):  # TODO
        pass

    def project(self):
        is_owner = Q(owner=self.owner)
        is_member = Q(mamber_user=self.owner)
        q = Project.objects.filter(is_owner | is_member)
        return q.distinct().order_by("name")

    def annotated_projects(self):
        project_ids = self.projects().values("id")

        q = Project.objects.filter(id_in=project_ids)
        n_down = Count("check", filter=Q(check_status="done"))
        q = q.annotate(n_down=n_down)
        return q.order_by("name")

    # @receiver(post_save, sender=User)
    # def create_user_profile(self, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(self, instance, **kwargs):
    #     instance.profile.save()


class Project(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(User, models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name or self.owner.email

    @property
    def owner_profile(self):
        return UserProfile.objects.for_user(self.owner)

    def team(self):
        return User.objects.filter(memberships_project=self).order_by("username")

    def invite(self, user):
        Member.objects.create(user=user, project=self)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Member(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="memberships")
    project = models.ForeignKey(Project, models.CASCADE)
