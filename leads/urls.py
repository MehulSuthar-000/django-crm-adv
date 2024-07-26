from django.urls import path
from  django.urls import include
import leads.views as views 


app_name = 'leads'
urlpatterns = [
    path('', views.lead_list, name='home'),
    path('create/', views.lead_create, name='lead-create'),
    path('<int:pk>/', views.lead_detail, name='lead-detail'),
    path('<int:pk>/update/', views.lead_update, name='lead-update'),
    path('<int:pk>/delete/', views.lead_delete, name='lead-delete'),
]
