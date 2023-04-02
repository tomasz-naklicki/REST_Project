from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class PokemonTypes(TextChoices):
    NORMAL = "NORMAL", _("Normal")
    FIRE = "FIRE", _("Fire")
    WATER = "WATER", _("Water")
    ELECTRIC = "ELECTRIC", _("Electric")
    GRASS = "GRASS", _("Grass")
    ICE = "ICE", _("Ice")
    FIGHTING = "FIGHTING", _("Fighting")
    POISON = "POISON", _("Poison")
    GROUND = "GROUND", _("Ground")
    FLYING = "FLYING", _("Flying")
    PSYCHIC = "PSYCHIC", _("Psychic")
    BUG = "BUG", _("Bug")
    ROCK = "ROCK", _("Rock")
    GHOST = "GHOST", _("Ghost")
    DRAGON = "DRAGON", _("Dragon")
    DARK = "DARK", _("Dark")
    STEEL = "STEEL", _("Steel")
    FAIRY = "FAIRY", _("Fairy")
