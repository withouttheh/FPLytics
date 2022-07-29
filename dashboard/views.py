from django.shortcuts import render
from django.http import HttpResponse

players = [ 
    {
        'name': 'Salah',
        'position': 'Midfield',
        'goals': 20,
    },
    {
        'name': 'Kane',
        'position': 'Forward',
        'goals': 22,
    },
    {   'name': 'Mane', 
        'position': 'Midfield',
        'goals': 25,
    }
]
 
# Logic for how to handle route the request to page
def dashboard(request): 
    context = { 
        'players': players
    }
    return render(request, 'dashboard/dashboard.html', context)