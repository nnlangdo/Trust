from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import District,Province,CashContributor,ChequeContributor,DraftContributor,KindContributor
from .forms import CashContributorForm,ChequeContributorForm,DraftContributorForm,KindContributorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def mode_donation(request):
    mode_donation = request.GET.get('mode_donation')
    context = {
        'mode_donation':mode_donation,
    }
    return render(request, 'partials/mode_donation.html',context)

def district(request):
    province = request.GET.get('state')
    districts = District.objects.filter(province=province)
    context = {
        'districts':districts,
    }
    return render(request, 'partials/district.html',context)
@login_required
def home(request):
    donations_cash_all = CashContributor.objects.all()
    donations_cash_user = CashContributor.objects.filter(received_by=request.user)
    donations_cheque_all = ChequeContributor.objects.all()
    donations_cheque_user = ChequeContributor.objects.filter(received_by=request.user)
    donations_draft_all = DraftContributor.objects.all()
    donations_draft_user = DraftContributor.objects.filter(received_by=request.user)
    donations_kind_all = KindContributor.objects.all()
    donations_kind_user = KindContributor.objects.filter(received_by=request.user)
    provinces = Province.objects.all()

    context = {
        'provinces':provinces,
        'donations_cash_user':donations_cash_user,
        'donations_cash_all':donations_cash_all,
        'donations_cheque_all':donations_cheque_all,
        'donations_cheque_user':donations_cheque_user,
        'donations_draft_all':donations_draft_all,
        'donations_draft_user':donations_draft_user,
        'donations_kind_all':donations_kind_all,
        'donations_kind_user':donations_kind_user,
    }
    return render(request, 'tellercounter/home.html', context)
@login_required
def add_cash(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = CashContributorForm(request.POST)
        if form.is_valid():
            teller_counter = form.save(commit=False)
            teller_counter.received_by = request.user
            teller_counter.save()
            # messages.add_message(request, messages.INFO, f'Donation completed successfuly')
            return redirect('tellercounter:receipt_cash', teller_counter_id_cash=teller_counter.id)
    else:
        form = CashContributorForm()

    context = {
        'form': form,
        'provinces':provinces,
    }
    return render(request, 'tellercounter/home.html', context)

@login_required
def add_cheque(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = ChequeContributorForm(request.POST)
        if form.is_valid():
            teller_counter = form.save(commit=False)
            teller_counter.received_by = request.user
            teller_counter.save()
            # messages.add_message(request, messages.INFO, f'Donation completed successfuly')
            return redirect('tellercounter:receipt_cheque', teller_counter_id_cheque=teller_counter.id)

    else:
        form = ChequeContributorForm()

    context = {
        'form': form,
        'provinces':provinces,
    }
    return render(request, 'tellercounter/home.html', context)

@login_required
def add_draft(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = DraftContributorForm(request.POST)
        if form.is_valid():
            teller_counter = form.save(commit=False)
            teller_counter.received_by = request.user
            teller_counter.save()
            # messages.add_message(request, messages.INFO, f'Donation completed successfuly')
            return redirect('tellercounter:receipt_draft', teller_counter_id_draft=teller_counter.id)

    else:
        form = DraftContributorForm()

    context = {
        'form': form,
        'provinces':provinces,
    }
    return render(request, 'tellercounter/home.html', context)

@login_required
def add_kind(request):
    provinces = Province.objects.all()
    if request.method == 'POST':
        form = KindContributorForm(request.POST)
        if form.is_valid():
            teller_counter = form.save(commit=False)
            teller_counter.received_by = request.user
            teller_counter.save()
            # messages.add_message(request, messages.INFO, f'Donation completed successfuly')
            return redirect('tellercounter:receipt_kind', teller_counter_id_kind=teller_counter.id)

    else:
        form = KindContributorForm()

    context = {
        'form': form,
        'provinces':provinces,
    }
    return render(request, 'tellercounter/home.html', context)

def receipt_cash(request,teller_counter_id_cash):
    data = get_object_or_404(CashContributor, id=teller_counter_id_cash)
    return render(request, 'tellercounter/receipt.html',{'data':data})
def receipt_cheque(request,teller_counter_id_cheque):
    data = get_object_or_404(ChequeContributor, id=teller_counter_id_cheque)
    return render(request, 'tellercounter/receipt.html',{'data':data})
def receipt_draft(request,teller_counter_id_draft):
    data = get_object_or_404(DraftContributor, id=teller_counter_id_draft)
    return render(request, 'tellercounter/receipt.html',{'data':data})
def receipt_kind(request,teller_counter_id_kind):
    data = get_object_or_404(KindContributor, id=teller_counter_id_kind)
    return render(request, 'tellercounter/receipt.html',{'data':data})
