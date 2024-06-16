from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel

from apps.profiles.models import Profile


class Rating(TimeStampedUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("poor")
        RATING_2 = 2, _("average")
        RATING_3 = 3, _("good")
        RATING_4 = 4, _("very good")
        RATING_5 = 5, _("excellent")

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User Ratings"),
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        related_name="agent_review",
        verbose_name=_("Agent being rated"),
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        choices=Range.choices,
        default=Range.RATING_2,
        help_text="1=poor,2=Fair,3=Good,4=Very Good, 5= Excellent",
        verbose_name=_("Rating"),
    )

    comment = models.TextField(verbose_name=_("Comment"))


class meta:
    unique_together = ["rater", "agent"]


def __str__(self):
    return f"{self.agent} rated at {self.rating}"
