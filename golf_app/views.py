from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Golfclub, Member, Tournament
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ClubListView(ListView):
    model = Golfclub
    template_name = 'club_list.html'
    context_object_name = 'all_clubs_list'

class TourListView(ListView):
    model = Tournament
    template_name = 'tour_list.html'
    context_object_name = 'all_tours_list'

class MemListView(ListView):
    model = Member
    template_name = 'mem_list.html'
    context_object_name = 'all_mems_list'

class ClubDetailView(DetailView):
    model = Golfclub
    template_name = 'club_detail.html'

class ClubCreateView(CreateView):
    model = Golfclub
    template_name = 'club_create.html'
    fields = ['name', 'location','year_established']

class TGListView(ListView):
    model = Tournament
    template_name = 'tg_list.html'
    context_object_name = 'all_tours_list'


def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'club_name': None,
        'error_message': None,
    }

    try:
        oldest_club = Golfclub.objects.earliest('year_established')
        context['club_name'] = oldest_club.name

    except Golfclub.DoesNotExist:
        context['error_message'] = "No clubs found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)


def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'members': None,
        'error_message': None,
    }

    try:
        # Retrieve all dogs and sort them by name in ascending order
        members = Member.objects.order_by('handicap')

        # Update the context with the list of dogs
        context['members'] = members

    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)


