from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


def summary_per_category(queryset):
    category_summary = OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))
    category_summary['Total'] = queryset.aggregate(total=Sum('amount'))['total']

    return category_summary
