from django_filters import rest_framework as filters

from main.models import Music


class MusicFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Music
        fields = ['category']

