from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView, DetailView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = 'snack_list_view.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail_view.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create_view.html'
    model = Snack
    fields = ["title","purchaser","description",]

class SnackUpdateView(UpdateView):
    template_name = 'snack_update_view.html'
    model = Snack
    fields = ['title','purchaser','description']

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete_view.html'
    model = Snack
    success_url = reverse_lazy('snack_list')