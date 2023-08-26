from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Province,District,CashContributor,ChequeContributor,DraftContributor,KindContributor
# Register your models here.

class ProvinceResource(resources.ModelResource):
   class Meta:
      model = Province
class ProvinceAdmin(ImportExportModelAdmin):
   resource_class = ProvinceResource
   list_display = ('id','name',)
   search_fields = ('name',)
admin.site.register(Province,ProvinceAdmin)

class DistrictResource(resources.ModelResource):
   class Meta:
      model = District
class DistrictAdmin(ImportExportModelAdmin):
   resource_class = DistrictResource
   list_display = ('id','name',)
   search_fields = ('name',)
admin.site.register(District,DistrictAdmin)

class CashContributorResource(resources.ModelResource):
    class Meta:
        model = CashContributor

class CashContributorAdmin(ImportExportModelAdmin):
    resource_class = CashContributorResource
    list_display = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','amt_cash','status','comment','date_created']
    search_fields = ('name',)

admin.site.register(CashContributor, CashContributorAdmin)

class ChequeContributorResource(resources.ModelResource):
    class Meta:
        model = ChequeContributor

class ChequeContributorAdmin(ImportExportModelAdmin):
    resource_class = ChequeContributorResource
    list_display = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','cheque_no',
                    'micr_cheque','date_cheque','amt_cheque','bank_cheque','status','comment','date_created']
    search_fields = ('name',)

admin.site.register(ChequeContributor, ChequeContributorAdmin)

class DraftContributorResource(resources.ModelResource):
    class Meta:
        model = DraftContributor

class DraftContributorAdmin(ImportExportModelAdmin):
    resource_class = DraftContributorResource
    list_display = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','draft_no','micr_draft','date_draft',
                    'amt_draft','bank_draft','status','comment','date_created']
    search_fields = ('name',)

admin.site.register(DraftContributor, DraftContributorAdmin)

class KindContributorResource(resources.ModelResource):
    class Meta:
        model = KindContributor

class KindContributorAdmin(ImportExportModelAdmin):
    resource_class = KindContributorResource
    list_display = ['id','name','mobile','state','district','village','pin','pan_no',
                    'mode_donation','kind_type',
                    'kind_wgt','kind_unit','status','comment','date_created']
    search_fields = ('name',)

admin.site.register(KindContributor, KindContributorAdmin)
