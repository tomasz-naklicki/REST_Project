from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from user.models import CustomUser
from .pokemontypes import PokemonTypes


# Move model
class Move(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Enter name of the move",
    )
    description = models.TextField(help_text="Enter move description")

    class MoveCategory(models.TextChoices):
        PHYSICAL = "PHYS", _("Physical")
        SPECIAL = "SPEC", _("Special")
        STATUS = "STAT", _("Status")

    category = models.CharField(
        max_length=4,
        help_text="Enter move category",
        choices=MoveCategory.choices,
    )
    type = models.CharField(
        max_length=8,
        help_text="Enter move type",
        choices=PokemonTypes.choices,
    )
    power = models.IntegerField(
        help_text="Enter move power if applicable",
        blank=True,
    )

    accuracy = models.IntegerField(
        help_text="Enter move accuracy if applicable",
        blank=True,
    )


# Team model
class Team(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=50, help_text="Enter a name for the team")

    def clean(self):
        if self.pokemon_set.count() > 6:
            raise ValidationError("A team can only have 6 Pokemon")


# Pokemon model
class Pokemon(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Enter Pokemon species name",
    )

    nickname = models.CharField(
        blank=True,
        max_length=20,
        help_text="Enter Pokemon nickname",
    )

    type1 = models.CharField(
        max_length=8,
        choices=PokemonTypes.choices,
        default=PokemonTypes.NORMAL,
        help_text="Enter first type of the Pokemon",
        verbose_name="First type",
    )

    type2 = models.CharField(
        max_length=8,
        choices=PokemonTypes.choices,
        blank=True,
        default="",
        help_text="Enter second type of the Pokemon",
        verbose_name="Second type",
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    hp = models.IntegerField(
        verbose_name="Health points",
    )
    atk = models.IntegerField(
        verbose_name="Attack",
    )

    spatk = models.IntegerField(
        verbose_name="Special attack",
    )

    defense = models.IntegerField(
        verbose_name="Defense",
    )

    spdef = models.IntegerField(
        verbose_name="Special defense",
    )

    spd = models.IntegerField(
        verbose_name="Speed",
    )

    moves = models.ManyToManyField(
        to=Move,
    )

    def save(self, *args, **kwargs):
        if self.moves.count() > 4:
            raise ValidationError(_("Pokemon can only learn 4 moves"))
        self.team.clean()
        return super().save(*args, **kwargs)
