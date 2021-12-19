from django.db import models
from django.utils.translation import gettext_lazy as _


class State(models.Model):
    """ Estado de la republica """
    name = models.CharField(_("Name"), max_length=50)
    state_code = models.IntegerField(_("Code"), primary_key=True, unique=True)  # ej. 01, 02, etc...
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.status = None

    def __str__(self):
        return self.name


class Municipality(models.Model):
    """ Municipio de un estado """
    name = models.CharField(_("Name"), max_length=100)
    municipality_code = models.IntegerField(_("Municipality"))  # ej. 001, 002, etc...
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_("State"))
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Municipality")
        verbose_name_plural = _("Municipalities")

    def __str__(self):
        return self.name


class Suburb(models.Model):
    """ Colonia de un municipio """
    name = models.CharField(_("Name"), max_length=100)
    settlement_type = models.CharField(_("Settlement type"), max_length=30)
    zip_code = models.CharField(_("Zip code"), max_length=5)  # ej. 20001, 20002, etc...
    zone_type = models.CharField(_("Zone type"), max_length=20)  # ej. Urbano, Rural
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name=_("Municipality"))
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Suburb")
        verbose_name_plural = _("Suburbs")

    def __str__(self):
        return self.name
