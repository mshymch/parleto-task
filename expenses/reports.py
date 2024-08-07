from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce, TruncMonth


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


def summary_per_year_month(queryset):
    year_month_summary = OrderedDict(sorted(
        queryset
        .annotate(year_month=TruncMonth('date'))
        .order_by()
        .values('year_month')
        .annotate(total=Sum('amount'))
        .values_list('year_month', 'total')
    ))

    return year_month_summary
