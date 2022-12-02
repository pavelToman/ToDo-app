from notes.models import Note, List
from rest_framework import viewsets
from rest_framework import permissions
from notes.serializers import NoteSerializer, ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lists to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer