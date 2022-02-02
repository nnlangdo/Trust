from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import TellerCounter
from .forms import TellerCounterForm

# Create your views here.
def home(request):
    form = TellerCounterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            district = form.cleaned_data['district']
            state = form.cleaned_data['state']
            pin = form.cleaned_data['pin']
            mobile = form.cleaned_data['mobile']
            mode_donation = form.cleaned_data['mode_donation']
            amt_cash = form.cleaned_data['amt_cash']
            cheque_no = form.cleaned_data['cheque_no']
            micr_cheque = form.cleaned_data['micr_cheque']
            draft_no = form.cleaned_data['draft_no']
            micr_draft = form.cleaned_data['micr_draft']
            kind_type = form.cleaned_data['kind_type']
            kind_wgt = form.cleaned_data['kind_wgt']
            kind_unit = form.cleaned_data['kind_unit']
            comment = form.cleaned_data['comment']
            data = TellerCounter(name=name,address=address,district=district,state=state,pin=pin,
            mobile=mobile,mode_donation=mode_donation,amt_cash=amt_cash,cheque_no=cheque_no,micr_cheque=micr_cheque,draft_no=draft_no,micr_draft=micr_draft,
            kind_type=kind_type,kind_wgt=kind_wgt,kind_unit=kind_unit,comment=comment)
            
            data.save()
            return HttpResponseRedirect('/')
        else:
            form = TellerCounterForm()
    return render(request, 'home.html', {'form':form})

def receiptpage(request):
    data = TellerCounter.objects.latest('date_created')
    return render(request, 'receipt.html',{'data':data})

def showdata(request):
    data = TellerCounter.objects.all()
    return render(request, 'showdata.html', {'data':data})
