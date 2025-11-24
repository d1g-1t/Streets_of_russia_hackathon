from rest_framework import viewsets
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели Contact'''
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
