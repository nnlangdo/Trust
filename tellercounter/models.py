from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
KIND_UNIT_CHOICE = (
    ('gram','gram'),
    ('kilogram','kilogram'),
)

MODE_DONATION_CHOICE = (
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


class TellerCounter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=30)
    state = models.CharField(choices=STATE_CHOICE,max_length=50)
    pin = models.CharField(blank=True,null=True,max_length=6)
    mobile = models.CharField(blank=True,null=True,max_length=10)
    mode_donation = models.CharField(choices=MODE_DONATION_CHOICE,max_length=10)
    amt_cash = models.CharField(blank=True,null=True, max_length=6)
    cheque_no = models.CharField(blank=True,null=True, max_length=6)
    micr_cheque = models.CharField(blank=True,null=True, max_length=9)
    draft_no = models.CharField(blank=True,null=True, max_length=6)
    micr_draft = models.CharField(blank=True,null=True, max_length=9)
    kind_type = models.CharField(blank=True,null=True,choices=KIND_TYPE_CHOICE,max_length=20)
    kind_wgt = models.CharField(blank=True,null=True,max_length=4)
    kind_unit = models.CharField(blank=True,null=True,choices=KIND_UNIT_CHOICE,max_length=10)
    comment = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    