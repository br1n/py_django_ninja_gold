from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    return render(request, 'ninja_gold/index.html')

def process(request):
    print "*"*50
    print request.POST['location']

    if request.method != "POST" or 'location' not in request.POST:
        return redirect('/')

    location_map = {
    'cave': random.randint(5, 10),
    'house': random.randint(2, 5),
    'farm': random.randint(10, 20),
    'casino': random.randint(-50, 50)
    }

    if request.POST['location'] not in location_map:
        return redirect('/')

    curr_gold = location_map[request.POST['location']]

    request.session['gold_count'] += curr_gold

    if curr_gold > 0:
        activity = {
        'content': "You won {} golds at the {}.".format(curr_gold, request.POST['location']),
        'css_class': 'green'
    }
        
    else:
        activity = {
        'content': "You lost {} gold at the {}.".format(curr_gold, request.POST['location']),
        'css_class': 'red'
    }

    request.session['activities'].insert(0, activity)
    request.session.modified = True
    
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')


# Create your views here.
