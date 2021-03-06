import django.forms.fields
from rest_framework import serializers
from rest_framework.fields import FileField

from .models import Mailbox, Email, Template


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = [
            'id', 'host', 'port', 'email_from', 'use_ssl', 'is_active', 'date', 'last_update'
        ]
        lookup_field = 'id'


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = [
            'id', 'subject', 'text', 'attachment', 'date', 'last_update'
        ]
        lookup_field = 'id'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = [
            'id', 'mailbox', 'template', 'to', 'cc', 'bcc', 'sent_date', 'date'
        ]
