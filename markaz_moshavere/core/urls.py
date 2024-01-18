from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login_reception, name='login'),
    path('logout', logout_reception, name='logout'),
    path('booking', book, name='book'),
    path('dashboard/<str:page>', dashboard_view, name='dash'),
    path('edit/<str:model>/<int:id>', edit, name='edit'),
    path('delete/<str:model>/<int:id>', delete, name='delete')
]
