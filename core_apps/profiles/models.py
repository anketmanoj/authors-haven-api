from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Profile(TimeStampedUUIDModel):
    class Gender(models.TextChoices):
        MALE = "male", _("male")
        FEMALE = "female", _("female")
        OTHER = "other", _("other")

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("phone number"), max_length=30, default="+811234567890")
    about_me = models.TextField(verbose_name=_("about me"), max_length=500, default="Say something about yourself")
    gender =  models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.MALE,
        max_length=20,
    )
    country = CountryField(verbose_name=_("country"), default="JP", blank=False, null=False)
    city = models.CharField(verbose_name=_("city"), max_length=180, default="Tokyo", null=False, blank=False)
    profile_photo = models.ImageField(verbose_name=_("profile photo"), default="/profile_default.jpg")
    twitter_handler = models.CharField(verbose_name=_("twitter handler"), max_length=50, blank=True)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def following_list(self):
        return self.follows.all()

    def followers_list(self):
        return self.followed_by.all()
    
    def follow(self, profile):
        self.follows.add(profile)
    
    def unfollow(self, profile):
        self.follows.remove(profile)

    def check_following(self, profile):
        return self.follows.filter(pkid=profile.pkid).exists()

    def check_is_followed_by(self, profile):
        return self.followed_by.filter(pkid=profile.pkid).exists()

