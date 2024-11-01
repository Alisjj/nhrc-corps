from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Case
from .forms import CaseForm, CaseEditForm
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Case
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        active_cases = Case.objects.filter(status=1).count()
        pending_cases = Case.objects.filter(status=2).count()
        resolved_cases = Case.objects.filter(status=3).count()
        
        context = {
            'active_cases': active_cases,
            'pending_cases': pending_cases,
            'resolved_cases': resolved_cases,
        }
        
        return render(request, self.template_name, context)

class CaseCreateView(CreateView, LoginRequiredMixin):
    model = Case
    form_class = CaseForm
    template_name = 'cases/case_form.html'
    success_url = reverse_lazy('cases:cases_list')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add'
        return context


class CaseUpdateView(UpdateView, LoginRequiredMixin):
    model = Case
    form_class = CaseEditForm
    template_name = 'cases/case_form.html'
    success_url = reverse_lazy('cases:cases_list')


@login_required
def cases_list(request):
    cases = Case.objects.all()
    paginator = Paginator(cases, 10)  # Show 10 cases per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cases/cases_list.html', {'cases': page_obj})