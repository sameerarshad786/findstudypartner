from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Room
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'rooms': Room.objects.all(),
    }
    return render(request, 'cmd1/home.html', context)

class RoomListView(ListView):
    template_name = 'cmd1/home.html'
    model = Room
    context_object_name = 'rooms'
    ordering = '-created_at'
    paginate_by = 5

class RoomDetailView(DetailView):
    template_name = 'cmd1/room-detail-page.html'

    def get_queryset(self):
        return Room.objects.all()

class RoomCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cmd1/create-room.html'
    model = Room
    fields = ['roomname', 'topics', 'about']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'cmd1/update-room.html'
    model = Room
    fields = ['roomname', 'topics', 'about']

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def test_func(self):
        room = self.get_object()
        if self.request.user == room.host:
            return True
        return False

class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'cmd1/delete-room.html'
    model = Room

    def test_func(self):
        room = self.get_object()
        if self.request.user == room.host:
            return True
        return False

    def get_success_url(self):
        return reverse('user-profile', kwargs={'pk': self.request.user.id})

def topics(request):
    context = {
        'rooms': Room.objects.all(),
        'title': 'Topics',
    }
    return render(request, 'cmd1/topics.html', context)