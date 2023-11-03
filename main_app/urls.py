from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.pops_index, name='index'),
    path('pops/<int:pop_id>/', views.pops_detail, name='detail'),
    path('pops/create/', views.PopCreate.as_view(), name='pops_create'),
    path('pops/<int:pk>/update/', views.PopUpdate.as_view(), name='pops_update'),
    path('pops/<int:pk>/delete/', views.PopDelete.as_view(), name='pops_delete'),
    path('pops/<int:pop_id>/add_logging/', views.add_logging, name='add_logging'),
    path('pops/<int:pop_id>/assoc_partner/<int:partner_id>/', views.assoc_partner, name='assoc_partner'),
    path('pops/<int:pop_id>/unassoc_partner/<int:partner_id>/', views.unassoc_partner, name='unassoc_partner'),
    path('partners/', views.PartnerList.as_view(), name='partners_index'),
    path('partners/<int:pk>/', views.PartnerDetail.as_view(), name='partners_detail'),
    path('partners/create/', views.PartnerCreate.as_view(), name='partners_create'),
    path('partners/<int:pk>/update/', views.PartnerUpdate.as_view(), name='partners_update'),
    path('partners/<int:pk>/delete/', views.PartnerDelete.as_view(), name='partners_delete'),
]