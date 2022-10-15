from django.contrib.auth import models as auth_models
from django.db import models
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
    NAME_MAX_LENGTH = 25

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    profile_pic = models.ImageField()

    short_bio = models.TextField()

    long_bio = models.TextField()

    advocate_years_exp = models.IntegerField()

    # company = models.ForeignKey('')
