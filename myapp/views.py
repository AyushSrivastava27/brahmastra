from django.shortcuts import render, HttpResponse, redirect
from .models import Event
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'POST':
            category = request.POST.get('category')
            event_name = request.POST.get('event_name')
            starting_date = request.POST.get('starting_date')
            ending_date = request.POST.get('ending_date')
            
            new_event = Event(category = category, event_name = event_name, starting_date = starting_date, ending_date = ending_date)
            new_event.save()
            return redirect('event')
        
def edit(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return redirect(request, 'event.html', context)

def update(request, id):
    
    if request.method == 'POST':

        category = request.POST.get('category')
        event_name = request.POST.get('event_name')
        starting_date = request.POST.get('starting_date')
        ending_date = request.POST.get('ending_date')
        
        new_event = Event(id = id, category = category, event_name = event_name, starting_date = starting_date, ending_date = ending_date)
        new_event.save()
        return redirect('event')
        
    return redirect(request, 'event.html')

def delete(request, id):
    events = Event.objects.filter(id = id).delete()
    context = {
        'events':events,
    }
    return redirect('event')

def event(request):
    
    events = Event.objects.all()
    context = {
        'events': events
    }
    print(context)
    return render(request, 'event.html', context)

    
    #         return HttpResponse('ADD EVENT SUCCESSFULLY')
        
    # elif request.method == 'GET':
    #         return render(request, 'event.html')
        
    # else:
    #     return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def sponsors(request):
    return render(request, 'sponsors.html')

def complaint(request):
    return render(request, 'complaint.html')

def organizer(request):
    return render(request, 'organizer.html')

def score(request):
    return render(request,'score.html')