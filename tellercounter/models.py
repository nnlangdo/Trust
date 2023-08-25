from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

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
    ('Other','Other')
)
STATUS_CHOICES = (
    ('live','live'),
    ('cancelled','cancelled'),
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

class Province(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class District(models.Model):
   name = models.CharField(max_length = 100)
   province = models.ForeignKey(Province,on_delete=models.SET_NULL,blank=True,null=True,related_name='distric_province',)
   class Meta:
        ordering = ['name']
        
   def __str__(self):
       return self.name

    
class CashContributor(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    village = models.CharField(max_length=100)
    pin = models.CharField(blank=True,null=True,max_length=6)
    mobile = models.CharField(blank=True,null=True,max_length=10)
    pan_no = models.CharField(blank=True,null=True,max_length=10)
    mode_donation = models.CharField(choices=MODE_DONATION_CHOICE,max_length=10)
    amt_cash = models.PositiveSmallIntegerField()
    status = models.CharField(choices=STATUS_CHOICES,default='live',max_length=9)
    comment = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    received_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    
    ordering = ['-date_created']
    def __str__(self):
        return self.name 
    
class ChequeContributor(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    village = models.CharField(max_length=100)
    pin = models.CharField(blank=True,null=True,max_length=6)
    mobile = models.CharField(blank=True,null=True,max_length=10)
    pan_no = models.CharField(blank=True,null=True,max_length=10)
    mode_donation = models.CharField(choices=MODE_DONATION_CHOICE,max_length=10)
    cheque_no = models.CharField(max_length=6)
    date_cheque = models.DateField()
    micr_cheque = models.CharField(max_length=9)
    amt_cheque = models.PositiveSmallIntegerField()
    status = models.CharField(choices=STATUS_CHOICES,default='live',max_length=9)
    comment = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    received_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    ordering = ['-date_created']
    def __str__(self):
        return self.name 
    
class DraftContributor(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    village = models.CharField(max_length=100)
    pin = models.CharField(blank=True,null=True,max_length=6)
    mobile = models.CharField(blank=True,null=True,max_length=10)
    pan_no = models.CharField(blank=True,null=True,max_length=10)
    mode_donation = models.CharField(choices=MODE_DONATION_CHOICE,max_length=10)
    draft_no = models.CharField(max_length=6)
    micr_draft = models.CharField(max_length=9)
    date_draft = models.DateField()
    amt_draft = models.PositiveSmallIntegerField()
    status = models.CharField(choices=STATUS_CHOICES,default='live',max_length=9)
    comment = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    received_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    
    ordering = ['-date_created']
    def __str__(self):
        return self.name 
    
class KindContributor(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    village = models.CharField(max_length=100)
    pin = models.CharField(blank=True,null=True,max_length=6)
    mobile = models.CharField(blank=True,null=True,max_length=10)
    pan_no = models.CharField(blank=True,null=True,max_length=10)
    mode_donation = models.CharField(choices=MODE_DONATION_CHOICE,max_length=10)
    kind_type = models.CharField(choices=KIND_TYPE_CHOICE,max_length=20)
    kind_wgt = models.CharField(blank=True,null=True,max_length=4)
    kind_unit = models.CharField(blank=True,null=True,choices=KIND_UNIT_CHOICE,max_length=10)
    status = models.CharField(choices=STATUS_CHOICES,default='live',max_length=9)
    comment = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    received_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    
    ordering = ['-date_created']
    def __str__(self):
        return self.name 