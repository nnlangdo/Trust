from random import choice
from django import forms
from .models import TellerCounter

KIND_UNIT_CHOICE = (
    ('gram','gram'),
    ('kilogram','kilogram'),
)

MODE_DONATION_CHOICE = (
    ('','Mode of donation'),
    ('Cash','Cash'),
    ('Cheque','Cheque'),
    ('Draft','Draft'),
    ('Kind','Kind'),
)

KIND_TYPE_CHOICE = (
    ('Silver Like Material','Silver Like Material'),
    ('Gold Like Material','Gold Like Material'),
    ('Other','Other Valueble')
)

STATE_CHOICE = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh	','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Dadra & Nagar Haveli and Daman & Diu','Dadra & Nagar Haveli and Daman & Diu'),
    ('Delhi','Delhi'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry'),
    ('Ladakh','Ladakh'),
)

class TellerCounterForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    district = forms.CharField()
    state = forms.ChoiceField(choices=STATE_CHOICE)
    pin = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    mode_donation = forms.ChoiceField(required=False,choices=MODE_DONATION_CHOICE)
    amt_cash = forms.CharField(required=False)
    cheque_no = forms.CharField(required=False)
    micr_cheque = forms.CharField(required=False)
    draft_no = forms.CharField(required=False)
    micr_draft = forms.CharField(required=False)
    kind_type = forms.ChoiceField(required=False,choices=KIND_TYPE_CHOICE)
    kind_wgt = forms.CharField(required=False)
    kind_unit = forms.ChoiceField(required=False,choices=KIND_UNIT_CHOICE)
    comment = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':3,'cols':3}))

