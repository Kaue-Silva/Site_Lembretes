from django.urls import path
from .views import index
from .views import new
from .views import update
from .views import delete
from .views import logout_page



urlpatterns = [
    path('', index, name='index'),
    path('novo lembrete', new, name='novo_lembrete'),
    path('novo lembrete/update/<int:id>', update, name='update'),
    path('novo lembrete/delete/<int:id>', delete, name='delete'),
    path('logout/', logout_page, name='logout'),
    
]
