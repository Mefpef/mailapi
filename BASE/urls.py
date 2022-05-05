from django.urls import path
from . import views


urlpatterns = [
    path('api/mailbox/', views.MailboxesView.as_view(), name='mailboxes'),
    path('api/mailbox/<uuid:id>', views.MailboxView.as_view(), name='mailbox'),
    path('api/templates/', views.TemplatesView.as_view(), name='templates'),
    path('api/template/<uuid:id>', views.TemplateView.as_view(), name='template'),
    path('api/email', views.MailView.as_view(), name='mail')
]