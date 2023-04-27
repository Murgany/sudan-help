from django.shortcuts import render, redirect
from .models import Request, MedicalService, MissingPerson
from .forms import RequestForm, MedicalServiceForm, MissingPersonForm
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    requests = Request.objects.all().order_by('-id')
    paginator = Paginator(requests, 10)  # Show 10 requests per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'index.html', context)


def medical_service_list(request):
    medical_services = MedicalService.objects.all().order_by('-id')
    paginator = Paginator(medical_services, 10)  # Show 10 medical services per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = MedicalServiceForm()
    if request.method == 'POST':
        form = MedicalServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('medical_services')
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'medical_service_list.html', context)

def missing_persons_reports(request):
    missing_persons_list = MissingPerson.objects.all().order_by('-reported_at')
    paginator = Paginator(missing_persons_list, 10)
    page = request.GET.get('page')
    missing_persons = paginator.get_page(page)
    if request.method == 'POST':
        form = MissingPersonForm(request.POST, request.FILES)
        if form.is_valid():
            missing_person = form.save(commit=False)
            missing_person.reported_by = request.user
            missing_person.save()
            return redirect('missing_persons')
    else:
        form = MissingPersonForm()
    return render(request, 'missing_persons.html', {'missing_persons': missing_persons, 'form': form})


def search_request(request):
    query = request.GET.get('q')
    context = {}
    if query:
        requests = Request.objects.filter(
            Q(request_type__icontains=query) | Q(item_name__icontains=query) | Q(address__icontains=query) | Q(
                phone_number__icontains=query) | Q(description__icontains=query))
        medical_services = MedicalService.objects.filter(
            Q(service_name__icontains=query) | Q(hospital_or_pharmacy_name__icontains=query) | Q(
                address__icontains=query) | Q(phone_number__icontains=query) | Q(description__icontains=query))
        missing_persons = MissingPerson.objects.filter(
            Q(report_type__icontains=query) | Q(name__icontains=query) | Q(age__icontains=query) | Q(
                gender__icontains=query) | Q(last_seen_location__icontains=query) | Q(
                reporters_phone_number__icontains=query) | Q(description__icontains=query))

        # Combine the querysets
        combined_results = list(requests) + list(medical_services) + list(missing_persons)

        paginator = Paginator(combined_results, 2)  # Change the number of items per page as per your requirements
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
    # return render(request, 'global_search.html', context)
    return render(request, 'search.html', context)
