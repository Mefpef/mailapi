from django_filters import rest_framework as filters
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin
from .filters import EmailFilter
from .serializers import MailboxSerializer, EmailSerializer, TemplateSerializer
from .models import Mailbox, Email, Template
import logging

logger = logging.getLogger('django')


class MailboxesView(ListCreateAPIView, ListModelMixin):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer

    def get(self, request, *args, **kwargs):
        logger.info('Mailbox displayed')
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info('Mailbox created')
        return self.create(request, *args, **kwargs)


class MailboxView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        logger.info('Single mailbox loaded successfully')
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        logger.info('Updated successfully')
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        logger.info('Partial updated successfully')
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info('MAILBOX deleted')
        return self.delete(request, *args, **kwargs)


class TemplatesView(ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        logger.info('Templates displayed')
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info('Mailbox created')
        return self.create(request, *args, **kwargs)


class TemplateView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        logger.info('Single mailbox loaded successfully')
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        logger.info('Updated successfully')
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        logger.info('Partial updated successfully')
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        logger.info('MAILBOX deleted')
        return self.delete(request, *args, **kwargs)


class MailView(ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmailFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
