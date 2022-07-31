from django.shortcuts import render
from django.http import HttpResponse

import requests
from requests.exceptions import HTTPError
import json
from datetime import date

# Create your views here. 
def home(request):
    
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    response = requests.get(url)
    gen_data = response.json()
    gw_name = gen_data['events'][0]['name']
    gw_deadline = gen_data['events'][0]['deadline_time'].split('T')
    #gw_name = 'Gameweek 1' 
    #gw_deadline = '2022-08-05T17:30:00Z'.split('T')
    deadline_date = date.fromisoformat(gw_deadline[0])
    deadline_time = gw_deadline[1][:5]


    context = {
        'gameweek': gw_name,
        'date': deadline_date, 
        'time': deadline_time
    }

    return render(request, 'home/index.html', context)
