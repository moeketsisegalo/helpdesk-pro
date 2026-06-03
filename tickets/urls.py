from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
# ]

from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'create-ticket/',
        views.create_ticket,
        name='create_ticket'
    ),
    path(
    'my-tickets/',
    views.my_tickets,
    name='my_tickets'
    ),
    path(
    'ticket/<int:ticket_id>/',
    views.ticket_detail,
    name='ticket_detail'
    ),
    path(
        'all-tickets/',
        views.all_tickets,
        name='all_tickets'
    ),
    path(
        'update-ticket/<int:ticket_id>/',
        views.update_ticket,
        name='update_ticket'
    ),
]