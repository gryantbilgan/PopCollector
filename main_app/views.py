from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pop, Partner
from .forms import LoggingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def pops_index(request):
    pops = Pop.objects.all()
    return render(request, 'pops/index.html', {
        'pops': pops
    })

def pops_detail(request, pop_id):
    pop = Pop.objects.get(id=pop_id)
    id_list = pop.partners.all().values_list('id')
    partners_pop_doesnt_have = Partner.objects.exclude(id_in=id_list)
    logging_form = LoggingForm()
    return render(request, 'pops/detail.html', {
        'pop': pop, 'logging_form': logging_form,
        'partners': partners_pop_doesnt_have
    })

class PopCreate(CreateView):
    model = Pop
    fields = '__all__'

class PopUpdate(UpdateView):
    model = Pop
    fields = ['brand', 'item_no', 'description']

class PopDelete(DeleteView):
    model = Pop
    success_url = '/pops'

def add_logging(request, pop_id):
    form = LoggingForm(request.POST)
    if form.is_valid():
        new_logging = form.save(commit=False)
        new_logging.pop_id = pop_id
        new_logging.save()
    return redirect('detail', pop_id=pop_id)

class PartnerList(ListView):
    model = Partner

class PartnerDetail(DetailView):
    model = Partner

class PartnerCreate(CreateView):
    model = Partner
    fields = '__all__'

class PartnerUpdate(UpdateView):
    model = Partner
    fields = ['name', 'item_no']

class PartnerDelete(DeleteView):
    model = Partner
    success_url = '/partners'

def assoc_partner(request, pop_id, partner_id):
    Pop.objects.get(id=pop_id).partners.add(partner_id)
    return redirect('detail', pop_id=pop_id)

def unassoc_partner(request, pop_id, partner_id):
    Pop.objects.get(id=pop_id).partners.remove(partner_id)
    return redirect('detail', pop_id=pop_id)