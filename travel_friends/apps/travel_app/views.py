from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import User
from .models import Trip

# Create your views here.
def travels(request):
    if 'user_id' not in request.session:
        print "The user is not in session"
        return redirect('/lr_app')
    else:
        print "user.id: " + str( User.objects.get(id=request.session['user_id']))
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'my_joins': Trip.objects.filter(members = User.objects.get(id=request.session['user_id'])),
            'my_trips': Trip.objects.filter(uploader = User.objects.get(id=request.session['user_id'])),
            'all_trips':  Trip.objects.exclude(uploader = User.objects.get(id=request.session['user_id'])).exclude(members = User.objects.get(id=request.session['user_id'])),
            # 'join_other_trips': Trip.objects__set.add(User.objects.get(id=request.session['user_id']))
        }
    return render(request, "dashboard.html", context)

def route_add_plan(request):
    return render(request, 'addplan.html')

def create_trip(request):
    new_trip = Trip.objects.trip_validation(request.POST)
    if new_trip[0]:
        print "A new trip should be in the database now..."
        return redirect('/travels')
    else:
        for err in new_trip[1]:
            messages.error(request, err)
        return redirect('/travels/route_add_plan')

def join_trip(request, id):
    this_trip = Trip.objects.get(id=id)
    curr_user = User.objects.get(id=request.session['user_id'])
    this_trip.members.add(curr_user)
    this_trip.save()
    curr_user.save()
    return redirect('/travels')

def destination(request, id):
    this_trip = Trip.objects.get(id=id)
    # not_this_user = Trip.objects.exclude(User.objects.get(id=3))
    all_members = this_trip.members.all() # Trip.objects.exclude(User.objects.get(id=request.session['user_id']))

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'destination': this_trip.destination,
        'description': this_trip.description,
        'uploader': this_trip.uploader,
        'start_date': this_trip.start_date,
        'end_date': this_trip.end_date,
        'travelers': all_members,
    }
    return render(request, 'destination.html', context)

    