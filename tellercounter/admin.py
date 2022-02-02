from django.contrib import admin
from .models import TellerCounter
# Register your models here.

@admin.register(TellerCounter)
class TellerCounterAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','district','state','pin','mobile','mode_donation','amt_cash','cheque_no','micr_cheque','draft_no','micr_draft','kind_type','kind_wgt','kind_unit','comment','date_created']
