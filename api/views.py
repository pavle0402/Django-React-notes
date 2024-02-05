from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        'Endpoint': '/notes/',
        'method': 'GET',
        'body': None,
        'description': 'Returns an array of notes'
    },
    {
        'Endpoint': '/notes/id',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single note object'
    },
    {
        'Endpoint': '/notes/create/',
        'method': 'POST',
        'body': {'body': ""},
        'description': 'Creates new note with data sent in post request'
    },
    {
        'Endpoint': '/notes/id/update/',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Creates an existing note with data sent in post request'
    },
    {
        'Endpoint': '/notes/id/delete/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes and exiting note'
    },
]
    return Response(routes)


@api_view(["GET"])
def getNotes(request):
    queryset = Note.objects.all()
    serializer = NoteSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request, pk):
    queryset = Note.objects.get(pk=pk)
    serializer = NoteSerializer(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body= data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateNote(request, pk):
    queryset = Note.objects.get(pk=pk)
    data = request.data
    serializer = NoteSerializer(instance=queryset, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return Response("Note was deleted!")

