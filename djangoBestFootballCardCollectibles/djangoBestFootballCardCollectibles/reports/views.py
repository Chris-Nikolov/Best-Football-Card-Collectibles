from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import ReportForm
from .models import Report
from ..cards.models import Card


class ReportListView(UserPassesTestMixin, ListView):
    model = Report
    template_name = 'reports/reports-page.html'
    context_object_name = 'reports'
    paginate_by = 4

    def test_func(self):
        return self.request.user.is_superuser


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report-card.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card'] = get_object_or_404(Card, id=self.kwargs['card_id'])
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.card = self.get_context_data()['card']
        response = super().form_valid(form)
        messages.success(self.request, "Report is sent successfully.")
        return response


class ReportDeleteView(UserPassesTestMixin, DeleteView):
    model = Report
    template_name = 'reports/delete-report.html'
    success_url = reverse_lazy('report-page')

    def test_func(self):
        return self.request.user.is_superuser
