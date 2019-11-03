from .models import Post

import django_filters


class UserFilter2(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['institute', 'instructor', 'rating', ]