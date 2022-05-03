from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MailboxSerializer, EmailSerializer, TemplateSerializer
from .models import Mailbox, Email, Template
from .filters import MailboxFilter
import logging
logger = logging.getLogger('django')


class MailboxesView(APIView):

    def get(self, request):
        mailboxes = Mailbox.objects.all()
        serializer = MailboxSerializer(mailboxes, many=True)
        logger.info('List of mailboxes load successfully')
        return Response(serializer.data)

    def post(self, request):
        serializer = MailboxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('POST successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MailboxView(APIView):

    def get(self, request, mailbox_id):
        mailbox = Mailbox.objects.get(id=mailbox_id)
        serializer = MailboxSerializer(mailbox)
        logger.info('Single mailbox loaded successfully')
        return Response(serializer.data)

    def put(self, request, mailbox_id):
        mailbox = Mailbox.objects.get(id=mailbox_id)
        serializer = MailboxSerializer(mailbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('POST successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, mailbox_id):
        mailbox = Mailbox.objects.get(id=mailbox_id)
        serializer = MailboxSerializer(mailbox, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info('PATCH successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mailbox_id):
        mailbox = Mailbox.objects.get(id=mailbox_id)
        mailbox.delete()
        logger.info('MAILBOX deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)


class TemplatesView(APIView):

    def get(self, request):
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        logger.info('List of templates load successfully')
        return Response(serializer.data)

    def put(self, request, templates_id):
        mailbox = Template.objects.get(id=templates_id)
        serializer = TemplateSerializer(mailbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('POST successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, templates_id):
        mailbox = Template.objects.get(id=templates_id)
        serializer = TemplateSerializer(mailbox, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info('PATCH successfully')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, templates_id):
        mailbox = Mailbox.objects.get(id=templates_id)
        mailbox.delete()
        logger.info('MAILBOX deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)