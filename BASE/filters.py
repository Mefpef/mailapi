from django_filters import rest_framework as filters
from .models import Email


class MailboxFilter(filters.FilterSet):
    class Meta:
        model = Email
        fields = ['sent_date']
