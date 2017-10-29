from django.shortcuts import render, redirect
from ..log_reg.models import *
from models import *
from django.contrib import messages
from datetime import date, datetime
from dateutil.parser import parse as parse_date


def travel_index(req):

    context = {
        'user_in_session': req.session['email_address'],
        'user_id': req.session['user_id'],
        'user': users.objects.get(id=req.session['user_id']),
        'trips' : travel.objects.all(),
        'joining':users.tag_along
    }
    return render(req, 'travelapp/traveldashboard.html', context)

def render_travel_form(req):
    print date.today()
    context = {
        'user_in_session': req.session['email_address']
    }

    return render(req, 'travelapp/traveladd.html', context)

def travel_add(req):
    errors = travel.objects.validate_trip(req.POST)

    if errors:
        for tag,error in errors.iteritems():
            messages.error(req,error,extra_tags=tag)
        return redirect('/travels/add')

    planner = users.objects.get(id=req.session['user_id'])

    new_trip = travel.objects.create(destination=req.POST['destination'],
                                     description=req.POST['description'],
                                     date_travel_from=req.POST['date_travel_from'],
                                     date_travel_to=req.POST['date_travel_to'],
                                     user_planner=planner
                                    )
    new_trip.save()

    return redirect('/travels')

def travel_details(req, travel_id):
    travel1 = travel.objects.get(id=travel_id)
    context = {
        'user_in_session': req.session['email_address'],
        'user_id': req.session['user_id'],
        'travel':travel1,
        'user': users.objects.get(id=req.session['user_id']),
        'tripname': travel1.destination,
        'plannername': travel1.user_planner.first_name,
        'plannerlastname': travel1.user_planner.last_name,
        'description': travel1.description,
        'datefrom': travel1.date_travel_from,
        'dateto': travel1.date_travel_to

    }

    return render(req, 'travelapp/travel.html',context)


def travel_join(req, travel_id):
    traveltojoin = travel.objects.get(id=travel_id)
    usertojoin = users.objects.get(id=req.session['user_id'])
    traveltojoin.user_joining.add(usertojoin)
    traveltojoin.save()

    return redirect('/travels')

# Create your views here.
