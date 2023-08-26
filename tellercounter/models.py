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
BANK_CHOICES = (
    ('Abhyudaya Co-op Bank','Abhyudaya Co-op Bank'),
    ('Allahabad Bank','Allahabad Bank'),
    ('Andhra Bank','Andhra Bank'),
    ('Apna Sahakari Bank','Apna Sahakari Bank'),
    ('Axis Bank','Axis Bank'),
    ('Bandhan Bank','Bandhan Bank'),
    ('Bank Of Baroda','Bank Of Baroda'),
    ('Bank of India','Bank of India'),
    ('Bank of Maharashtra','Bank of Maharashtra'),
    ('Bhartiya Mahila Bank','Bhartiya Mahila Bank'),
    ('Canara Bank','Canara Bank'),
    ('Central Bank of India','Central Bank of India'),
    ('Citi bank','Citi bank'),
    ('Corporation Bank','Corporation Bank'),
    ('DCB Bank','DCB Bank'),
    ('Federal Bank','Federal Bank'),
    ('Grameen Bank','Grameen Bank'),
    ('Gujarat State Co-op Bank','Gujarat State Co-op Bank'),
    ('Hasti Co-op Bank','Hasti Co-op Bank'),
    ('HDFC Bank','HDFC Bank'),
    ('ICICI Bank','ICICI Bank'),
    ('IDBI Bank','IDBI Bank'),
    ('IDFC Bank','IDFC Bank'),
    ('Indian Bank','Indian Bank'),
    ('Indian Overseas Bank','Indian Overseas Bank'),
    ('IndusInd Bank','IndusInd Bank'),
    ('ING Vysya Bank','ING Vysya Bank'),
    ('Janata Sahakari Bank','Janata Sahakari Bank'),
    ('Karnataka Bank','Karnataka Bank'),
    ('Karur Vysya Bank','Karur Vysya Bank'),
    ('Kotak Mahindra Bank','Kotak Mahindra Bank'),
    ('Mehsana Urban Co-op Bank','Mehsana Urban Co-op Bank'),
    ('Nainital Bank','Nainital Bank'),
    ('NKGSB Co-op Bank','NKGSB Co-op Bank'),
    ('Oriental Bank of Commerce','Oriental Bank of Commerce'),
    ('Others','Others'),
    ('Post Office','Post Office'),
    ('Punjab & Maharashtra Co-op Bank','Punjab & Maharashtra Co-op Bank'),
    ('Punjab National Bank','Punjab National Bank'),
    ('Punjab & Sind Bank','Punjab & Sind Bank'),
    ('RBL Bank','RBL Bank'),
    ('Saraswat Bank','Saraswat Bank'),
    ('State Bank of Bikaner & Jaipur','State Bank of Bikaner & Jaipur'),
    ('State Bank of Hyderabad','State Bank of Hyderabad'),
    ('State Bank Of India','State Bank Of India'),
    ('State Bank of Mysore','State Bank of Mysore'),
    ('State Bank of Patiala','State Bank of Patiala'),
    ('State Bank of Travancore','State Bank of Travancore'),
    ('Syndicate Bank','Syndicate Bank'),
    ('Tamilnad Mercantile Bank','Tamilnad Mercantile Bank'),
    ('The South Indian Bank','The South Indian Bank'),
    ('UCO Bank','UCO Bank'),
    ('Union Bank of India','Union Bank of India'),
    ('United Bank of India','United Bank of India'),
    ('Vijaya Bank','Vijaya Bank'),
    ('Yes Bank','Yes Bank'),
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
    bank_cheque = models.CharField(max_length=50,choices=BANK_CHOICES, blank=True, null=True)
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
    bank_draft = models.CharField(max_length=50,choices=BANK_CHOICES, blank=True, null=True)
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