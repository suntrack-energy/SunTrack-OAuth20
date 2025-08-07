from django.urls import path
from apps.users.views import login, cadastrar, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastrar, name='cadastrar'),
    path('logout/', logout, name='logout'),
]