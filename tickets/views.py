from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TicketForm
from .models import Ticket
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .admin_forms import TicketStatusForm
# @login_required
# def dashboard(request):

#     return render(
#         request,
#         'dashboard.html'
#     )

# @login_required
# def dashboard(request):

#     open_tickets = Ticket.objects.filter(
#         status='Open'
#     ).count()

#     in_progress = Ticket.objects.filter(
#         status='In Progress'
#     ).count()

#     closed_tickets = Ticket.objects.filter(
#         status='Closed'
#     ).count()

#     context = {
#         'open_tickets': open_tickets,
#         'in_progress': in_progress,
#         'closed_tickets': closed_tickets,
#     }

#     return render(
#         request,
#         'dashboard.html',
#         context
#     )
@login_required
def create_ticket(request):

    if request.method == 'POST':

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.created_by = request.user

            ticket.save()

            return redirect('dashboard')

    else:

        form = TicketForm()

    return render(
        request,
        'create_ticket.html',
        {
            'form': form
        }
    )

@login_required
def my_tickets(request):

    tickets = Ticket.objects.filter(
        created_by=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_tickets.html',
        {
            'tickets': tickets
        }
    )
@login_required
def ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        created_by=request.user
    )

    return render(
        request,
        'ticket_detail.html',
        {
            'ticket': ticket
        }
    )

@staff_member_required
def all_tickets(request):

    query = request.GET.get('q')

    tickets = Ticket.objects.all()

    if query:

        tickets = tickets.filter(
            title__icontains=query
        )

    tickets = tickets.order_by('-created_at')

    return render(
        request,
        'all_tickets.html',
        {
            'tickets': tickets,
            'query': query
        }
    )
@staff_member_required
def update_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if request.method == 'POST':

        form = TicketStatusForm(
            request.POST,
            instance=ticket
        )

        if form.is_valid():

            form.save()

            return redirect('all_tickets')

    else:

        form = TicketStatusForm(
            instance=ticket
        )

    return render(
        request,
        'update_ticket.html',
        {
            'ticket': ticket,
            'form': form
        }
    )

from .models import Ticket

@login_required
def dashboard(request):

    open_tickets = Ticket.objects.filter(status='Open').count()

    in_progress = Ticket.objects.filter(
        status='In Progress'
    ).count()

    closed_tickets = Ticket.objects.filter(
        status='Closed'
    ).count()

    total_tickets = Ticket.objects.count()

    recent_tickets = Ticket.objects.order_by(
        '-created_at'
    )[:5]

    return render(
        request,
        'dashboard.html',
        {
            'open_tickets': open_tickets,
            'in_progress': in_progress,
            'closed_tickets': closed_tickets,
            'total_tickets': total_tickets,
            'recent_tickets': recent_tickets,
        }
    )