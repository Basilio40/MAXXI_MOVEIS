from django.urls import path

from backend.logistica import views as v

app_name = 'logistica'

urlpatterns = [
    path('', v.ListEntrega.as_view(), name='entrega'),
    path('itens_entrega',v.ItensEntrega,name='itens_entrega'),
    
]