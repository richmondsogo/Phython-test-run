from typing import List
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from .forms import NotesForm
from .models import Notes


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes 
    success_url = '/smart/notes'
    form_class = NotesForm     

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'
    form_class = NotesForm 
    login_url = '/admin'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model =  Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self): 
        return Notes.objects.filter(user=self.request.user)


class NotesDetailView(DetailView):
    model =  Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
