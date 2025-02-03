from django.db import models as django_models
from django.utils.translation import gettext_lazy as _


class Model(django_models.Model):
    criado_em = django_models.DateTimeField(auto_now_add=True, verbose_name=_('criado em'))
    alterado_em = django_models.DateTimeField(auto_now=True, verbose_name=_('alterado em'))

    class BaseMeta:
        get_latest_by = ('criado_em', 'alterado_em')

    class Meta(BaseMeta):
        abstract = True