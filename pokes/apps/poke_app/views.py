from django.shortcuts import render, redirect
from django.contrib import messages
from ..login.models import User
# from .models import Trip

# Create your views here.
def pokes(request):
    # if 'user_id' not in request.session:
    #     print "The user is not in session"
    #     return redirect('/lr_app')
    # else:
    #     print "user.id: " + str( User.objects.get(id=request.session['user_id']))

    context = {
        'user': User.objects.get(id=request.session['user_id']),
#         'my_joins': Trip.objects.exclude(uploader_id = User.objects.get(id=request.session['user_id'])),
#         'my_trips': Trip.objects.filter(uploader_id = User.objects.get(id=request.session['user_id'])),
#         'other_trips':  Trip.objects.exclude(uploader = User.objects.get(id=request.session['user_id'])).exclude(members = User.objects.get(id=request.session['user_id'])),
#         # 'join_other_trips': Trip.objects__set.add(User.objects.get(id=request.session['user_id']))
    }

    return render(request, "dashboard.html", context)