from django.urls import path
from . import views

app_name = "tellercounter"

urlpatterns = [
    # ... Your other URLs ...
    path('', views.home, name='home'),
    path('district/', views.district, name='district'),
    path('mode_donation/', views.mode_donation, name='mode_donation'),
    path('add_cash/', views.add_cash, name='add_cash'),
    path('add_cheque/', views.add_cheque, name='add_cheque'),
    path('add_draft/', views.add_draft, name='add_draft'),
    path('add_kind/', views.add_kind, name='add_kind'),
    path('receipt_cash/<int:teller_counter_id_cash>/', views.receipt_cash, name='receipt_cash'),
    path('receipt_cheque/<int:teller_counter_id_cheque>/', views.receipt_cheque, name='receipt_cheque'),
    path('receipt_draft/<int:teller_counter_id_draft>/', views.receipt_draft, name='receipt_draft'),
    path('receipt_kind/<int:teller_counter_id_kind>/', views.receipt_kind, name='receipt_kind'),
]
