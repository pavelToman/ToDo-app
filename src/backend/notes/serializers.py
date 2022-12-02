from rest_framework import serializers

from .models import List, Note


class ListSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['name', 'url', 'notes']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['list', 'text', 'done', 'due_date', 'url']