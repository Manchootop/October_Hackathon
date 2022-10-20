from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

from Octomber_Hackathon.auth_app.managers import AdvocateUserManager

'''
{
    "id":1,
    "name":"Dennis Ivy",
    "profile_pic":"/user_pic.png",
    "short_bio":"...",
    "long_bio":"...",
    "advocate_years_exp":1,
    "company":{
        "id":6,
        "name":"Agora",
        "logo":"agora_logo.png",
        "href":"/companies/6",
    },
    "links":{
        "youtube":"youtube.com/username",
        "twitter":"twitter.com/username",
        "github":"github.com/username",
    }
}'''


class AdvocateUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True)

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'email'

    objects = AdvocateUserManager()


class AdvocateProfile(models.Model):
    NAME_MAX_LENGTH = 25

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    profile_pic = models.ImageField()

    short_bio = models.TextField()

    long_bio = models.TextField()

    advocate_years_exp = models.IntegerField()

    user = models.ForeignKey(AdvocateUser, on_delete=models.CASCADE, primary_key=True)

