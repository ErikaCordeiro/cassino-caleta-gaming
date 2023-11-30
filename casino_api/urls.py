from django.urls import path
from wallet import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('balance/', views.balance_view, name='balance'),
    path('bet/', views.bet_view, name='bet'),
    path('win/', views.win_view, name='win'),
    path('rollback/', views.rollback_view, name='rollback'),
]
