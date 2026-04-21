from django.shortcuts import render
from django.http import Http404
from . models import Notes  

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return render(request, 'notes/note_not_found.html', {'note_id': pk})   
    return render(request, 'notes/notes_details.html', {'note': note})