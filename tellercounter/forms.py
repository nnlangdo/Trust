from random import choice
from django import forms
from .models import CashContributor,ChequeContributor,DraftContributor,KindContributor


class CashContributorForm(forms.ModelForm):
    class Meta:
        model = CashContributor
        fields = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','amt_cash']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}), 
            'district': forms.Select(attrs={'class':'form-control'}),
            'village': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'mode_donation': forms.Select(attrs={'class':'form-control'}),
            'amt_cash': forms.NumberInput(attrs={'class':'form-control','max':199999,'required':'true'}),
        }

class ChequeContributorForm(forms.ModelForm):
    class Meta:
        model = ChequeContributor
        fields = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','cheque_no',
                    'micr_cheque','date_cheque','amt_cheque','bank_cheque']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}), 
            'district': forms.Select(attrs={'class':'form-control'}),
            'village': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'mode_donation': forms.Select(attrs={'class':'form-control'}),
            'cheque_no': forms.TextInput(attrs={'class':'form-control'}),
            'micr_cheque': forms.TextInput(attrs={'class':'form-control'}),
            'date_cheque': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'amt_cheque': forms.NumberInput(attrs={'class':'form-control','type':'number'}),
            'bank_cheque': forms.Select(attrs={'class':'form-control'}),
            # 'status': forms.Select(attrs={'class':'form-control'}),
            # 'comment': forms.Textarea(attrs={'class':'form-control'}),
        }

class DraftContributorForm(forms.ModelForm):
    class Meta:
        model = DraftContributor
        fields = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','draft_no','micr_draft','date_draft','amt_draft','bank_draft']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}), 
            'district': forms.Select(attrs={'class':'form-control'}),
            'village': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'mode_donation': forms.Select(attrs={'class':'form-control'}),
            'draft_no': forms.TextInput(attrs={'class':'form-control'}),
            'micr_draft': forms.TextInput(attrs={'class':'form-control'}),
            'date_draft': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'amt_draft': forms.NumberInput(attrs={'class':'form-control','type':'number'}),
            'bank_draft': forms.Select(attrs={'class':'form-control'}),
            # 'status': forms.Select(attrs={'class':'form-control'}),
            # 'comment': forms.Textarea(attrs={'class':'form-control'}),
        }

class KindContributorForm(forms.ModelForm):
    class Meta:
        model = KindContributor
        fields = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation',
                    'kind_type',
                    'kind_wgt','kind_unit']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}), 
            'district': forms.Select(attrs={'class':'form-control'}),
            'village': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.TextInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'mode_donation': forms.Select(attrs={'class':'form-control'}),
            'kind_type': forms.Select(attrs={'class':'form-control'}),
            'kind_wgt': forms.TextInput(attrs={'class':'form-control'}),
            'kind_unit': forms.Select(attrs={'class':'form-control'}),
            # 'status': forms.Select(attrs={'class':'form-control'}),
            # 'comment': forms.Textarea(attrs={'class':'form-control'}),
        }
