from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Odredfield(models.PositiveBigIntegerField):
    '''Порядок следование'''

    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                queryset = self.model.objects.all()
                if self.for_fields:
                    query = {field: getattr(model_instance, field)
                             for field in self.for_fields}
                    queryset = queryset.filter(**query)
                last_item = queryset.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
