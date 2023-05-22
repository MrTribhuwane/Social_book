from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.name = 'Pune'
    dest1.desc = 'One of the best city in India'
    dest1.price = 1200
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name= 'Mumbai'
    dest2.desc= 'City which never sleeps'
    dest2.price= 1150
    dest1.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name= 'Nashik'
    dest3.desc= 'JEVLIS KA'
    dest3.price= 1000
    dest1.img = 'destination_3.jpg'

    dests = [dest1,dest2,dest3]

    return render(request,"index.html",{'dests':dests})